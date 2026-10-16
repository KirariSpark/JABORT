from PySide6.QtWidgets import QWidget, QMessageBox

from workers import FlattenWorker, NewFlattenWorker, worker_manager
from pages.file_mgr.ui_page import Ui_FileMgrTab
from core.error_codes import ErrorCode
from modules.utils import ui_utils
from core import app_config

class FileMgrWidget(QWidget, Ui_FileMgrTab):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.flatten_worker = None
        self.setupUi(self)

        # 绑定信号
        self.FlattenRun.clicked.connect(self.flatten_run)
        self.FlattenStop.clicked.connect(lambda: self.flatten_worker.stop())
        self.FlattenDirOpen.clicked.connect(lambda: ui_utils.select_folder(self, self.FlattenDirInput))
        self.NewFlattenRun.clicked.connect(self.new_flatten_run)
        self.NewFlattenStop.clicked.connect(lambda: worker_manager.request_stop())
        self.NewFlattenDirOpen.clicked.connect(lambda: ui_utils.select_folder(self, self.NewFlattenDirInput))

    def flatten_run(self):
        self.FlattenRun.setEnabled(False)
        self.FlattenStop.setEnabled(True)
        self.flatten_worker = FlattenWorker(self.FlattenDirInput.text(), app_config.get_conflict_mode())
        self.flatten_worker.worker_finished.connect(lambda: self.FlattenRun.setEnabled(True))
        self.flatten_worker.worker_finished.connect(lambda: self.FlattenStop.setEnabled(False))
        self.flatten_worker.worker_finished.connect(lambda t: ui_utils.show_message_box(self, t[0], t[1], t[2]))
        self.flatten_worker.start()

    def new_flatten_run(self):
        if worker_manager.is_busy():
            ui_utils.show_message_box(self, "提示", ErrorCode.WorkerBusy.generic, QMessageBox.Icon.Warning)
            return
        self.NewFlattenRun.setEnabled(False)
        self.NewFlattenStop.setEnabled(True)
        worker = NewFlattenWorker(self.NewFlattenDirInput.text(), app_config.get_conflict_mode())
        # 连接到主线程 QObject 的绑定方法，保证回调在主线程执行（详见 WorkerManager.submit 文档）
        worker.progress_updated.connect(self.NewFlattenProgress.setValue)
        worker.worker_finished.connect(self.on_new_flatten_finished)
        if not worker_manager.submit(worker):
            self.NewFlattenRun.setEnabled(True)
            self.NewFlattenStop.setEnabled(False)

    def on_new_flatten_finished(self, result: tuple):
        self.NewFlattenRun.setEnabled(True)
        self.NewFlattenStop.setEnabled(False)
        ui_utils.show_message_box(self, result[0], result[1], result[2])