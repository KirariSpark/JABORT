from PySide6.QtWidgets import QWidget, QMessageBox

from workers import FlattenWorker, NewFlattenWorker, worker_manager
from core.error_codes import ErrorCode
from pages.file_mgr.ui_page import Ui_FileMgrWidget
from modules.utils import ui_utils
from core import app_config

class FileMgrWidget(QWidget, Ui_FileMgrWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.flatten_worker = None
        self.setupUi(self)

        # 绑定信号
        self.FlattenRun.clicked.connect(self.new_flatten_run)
        self.FlattenStop.clicked.connect(lambda: worker_manager.request_stop())
        self.FlattenDirOpen.clicked.connect(lambda: ui_utils.select_folder(self, self.FlattenDirInput))

    def new_flatten_run(self):
        if worker_manager.is_busy():
            ui_utils.show_message_box(self, "提示", ErrorCode.WorkerBusy.generic, QMessageBox.Icon.Warning)
            return
        self.FlattenRun.setEnabled(False)
        self.FlattenStop.setEnabled(True)
        worker = NewFlattenWorker(self.FlattenDirInput.text(), app_config.get_conflict_mode())
        # 连接到主线程 QObject 的绑定方法，保证回调在主线程执行（详见 WorkerManager.submit 文档）
        worker.progress_updated.connect(self.FlattenProgress.setValue)
        worker.worker_finished.connect(self.on_new_flatten_finished)
        if not worker_manager.submit(worker):
            self.FlattenRun.setEnabled(True)
            self.FlattenStop.setEnabled(False)

    def on_new_flatten_finished(self, result: tuple):
        self.FlattenRun.setEnabled(True)
        self.FlattenStop.setEnabled(False)
        ui_utils.show_message_box(self, result[0], result[1], result[2])