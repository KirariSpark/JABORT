from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QMessageBox

from core.error_codes import ErrorCode
from core.logger import logger


class WorkerBase(QObject):
    """后台工作对象基类。

    所有具体 worker 均为 QObject，由 WorkerManager 通过 moveToThread 投递到
    全局唯一的后台线程执行。子类只需实现 task()，不需要（也不应该）重写 run()。
    """
    # 结束信号，第一项为标题，第二项为内容，第三项为图标
    worker_finished = Signal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._stop = False
        self._finished = False

    def stop(self):
        """请求停止。

        必须是普通方法（直接置位标志），不能是队列连接的槽——task() 执行期间
        后台线程的事件循环被阻塞，队列槽永远不会被处理。
        """
        self._stop = True

    @Slot()
    def execute(self):
        """后台线程入口，由 WorkerManager 通过 invokeMethod 调用。

        包裹 task()，保证 worker_finished 恰好发射一次，即使 task() 抛出异常
        也能清掉 WorkerManager 的忙标志，避免任务系统卡死。
        """
        self._stop = False
        self._finished = False
        try:
            self.task()
        except Exception as e:
            logger.critical(f"Worker 发生未捕获异常：{e}")
            self.finish("严重错误", ErrorCode.Unknown.format(str(e)), QMessageBox.Icon.Critical)
        finally:
            if not self._finished:
                logger.error("Worker 未报告完成，已强制结束")
                self.finish("错误", ErrorCode.Unknown.generic, QMessageBox.Icon.Critical)

    def finish(self, title: str, content: str, icon: QMessageBox.Icon):
        """结束任务时调用，保证只发射一次 worker_finished。"""
        if self._finished:
            return
        self._finished = True
        self.worker_finished.emit((title, content, icon))

    def task(self):
        """子类实现：任务主体。"""
        raise NotImplementedError
