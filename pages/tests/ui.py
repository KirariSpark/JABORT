from PySide6.QtWidgets import QWidget, QMessageBox

from workers import ImageSeqWorker, worker_manager
from core.error_codes import ErrorCode
from modules.tests.QtIconExport import export_all_icons
from modules.utils import ui_utils
from pages.tests.ui_page import Ui_TestTab


class TestsWidget(QWidget, Ui_TestTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # 绑定信号
        self.IconExport.clicked.connect(self.export_icons)
        self.IconOutputOpen.clicked.connect(lambda: ui_utils.select_folder(self, self.IconOutputPath))
        self.SeqStart.clicked.connect(self.image_seq_gen_run)
        self.SeqStop.clicked.connect(lambda: worker_manager.request_stop())
        self.SeqPathOpen.clicked.connect(lambda: ui_utils.select_folder(self, self.SeqPathInput))

    def image_seq_gen_run(self):
        if worker_manager.is_busy():
            ui_utils.show_message_box(self, "提示", ErrorCode.WorkerBusy.generic, QMessageBox.Icon.Warning)
            return
        self.SeqStop.setEnabled(True)
        self.SeqStart.setEnabled(False)
        worker = ImageSeqWorker(
            num_images=self.SeqItemAmount.value(),
            output_folder=self.SeqPathInput.text()
        )
        # 注意：worker 被 moveToThread 到后台线程后，连接用的槽必须绑定在主线程的
        # QObject（这里是 self 和控件）上。若用 lambda/普通函数连接，Qt 会在后台线程
        # 里直接调用它们（没有接收者），导致 GUI 操作跨线程、消息框卡死。
        worker.progress_updated.connect(self.SeqProgress.setValue)
        worker.worker_finished.connect(self.on_seq_finished)
        if not worker_manager.submit(worker):
            self.SeqStart.setEnabled(True)
            self.SeqStop.setEnabled(False)

    def on_seq_finished(self, result: tuple):
        self.SeqStart.setEnabled(True)
        self.SeqStop.setEnabled(False)
        ui_utils.show_message_box(self, result[0], result[1], result[2])

    def export_icons(self):
        res = export_all_icons(self.IconOutputPath.text())
        if res[1]:
            ui_utils.show_message_box(self, content=f"导出已完成\n成功 {res[0]}\n失败 {res[1]}",
                                      icon=QMessageBox.Icon.Warning)
        else:
            ui_utils.show_message_box(self, content=f"导出已完成\n成功 {res[0]}\n失败 {res[1]}",
                                      icon=QMessageBox.Icon.Information)
