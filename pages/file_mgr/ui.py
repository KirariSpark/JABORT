from PySide6.QtWidgets import QWidget

from Workers import FlattenWorker, NewFlattenWorker
from pages.file_mgr.ui_page import Ui_FileMgrWidget
from modules.utils import ui_utils
from core import app_config

class FileMgrWidget(QWidget, Ui_FileMgrWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.new_flatten_worker = None
        self.flatten_worker = None
        self.setupUi(self)

        # 绑定信号
        self.FlattenRun.clicked.connect(self.new_flatten_run)
        self.FlattenStop.clicked.connect(lambda: self.new_flatten_worker.stop())
        self.FlattenDirOpen.clicked.connect(lambda: ui_utils.select_folder(self, self.FlattenDirInput))

    def new_flatten_run(self):
        self.FlattenRun.setEnabled(False)
        self.FlattenStop.setEnabled(True)
        self.new_flatten_worker = NewFlattenWorker(self.FlattenDirInput.text(), app_config.get_conflict_mode())