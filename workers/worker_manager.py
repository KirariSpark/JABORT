from PySide6.QtCore import QObject, QThread, QMetaObject, Qt, Slot

from core.logger import logger


class WorkerManager(QObject):
    """全局唯一的后台工作线程管理器。

    整个程序只有一条后台 QThread；同一时刻只接受一个任务；线程忙时
    submit() 返回 False（不入队），由调用方决定如何提示。
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._thread: QThread | None = None
        self._busy = False
        self._current = None

    def _ensure_thread(self):
        """首次提交任务时才创建并启动后台线程，避免在 QApplication 之前建线程。"""
        if self._thread is None:
            self._thread = QThread()
            self._thread.start()
            logger.debug("后台工作线程已启动")

    def is_busy(self) -> bool:
        """当前是否有任务正在执行。"""
        return self._busy

    def submit(self, worker) -> bool:
        """尝试把 worker 投递到后台线程执行。

        忙时拒绝并返回 False，否则把 worker 移到后台线程并排队调用其
        execute() 槽，返回 True。调用方需在 submit 之前连接好所需信号。

        重要：worker 被 moveToThread 到后台线程后，它的信号只能连接到
        主线程 QObject 的绑定方法（如 self.on_finished、widget.setValue）。
        如果连接到 lambda/普通函数，Qt 找不到接收者，会直接在后台线程里
        调用它，导致 GUI 跨线程操作、消息框卡死等问题。
        """
        if self._busy:
            logger.warning("后台线程正忙，拒绝新任务")
            return False
        self._ensure_thread()
        self._busy = True
        self._current = worker
        worker.moveToThread(self._thread)
        worker.worker_finished.connect(self._on_finished)
        QMetaObject.invokeMethod(worker, "execute", Qt.ConnectionType.QueuedConnection)
        return True

    @Slot(tuple)
    def _on_finished(self, _result: tuple):
        """任务结束时清掉忙标志，并回收 worker。"""
        worker = self._current
        self._current = None
        self._busy = False
        if worker is not None:
            worker.deleteLater()

    def request_stop(self):
        """请求终止当前任务。"""
        if self._current is not None:
            self._current.stop()

    def shutdown(self):
        """退出程序时停止后台线程。"""
        if self._thread is None:
            return
        if self._current is not None:
            self._current.stop()
        self._thread.quit()
        if self._thread.wait(5000):
            logger.debug("后台工作线程已退出")
        else:
            logger.warning("后台工作线程未能在 5 秒内退出")


# 模块级单例：全程序共用唯一后台工作线程
worker_manager = WorkerManager()
