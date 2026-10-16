from PySide6.QtWidgets import QWidget, QMessageBox

from workers import ImgSeq2PDFWorker, PNG2JPGWorker, worker_manager
from pages.converters.ui_page import Ui_ConverterWidget
from core.error_codes import ErrorCode
from modules.utils import ui_utils
from core import app_config

class ConverterWidget(QWidget, Ui_ConverterWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        # PNG转JPG信号
        self.PNG2JPGRun.clicked.connect(self.png2jpg_run)
        self.PNG2JPGStop.clicked.connect(lambda: worker_manager.request_stop())
        self.PNG2JPGFindDir.clicked.connect(lambda: ui_utils.select_folder(self, self.PNG2JPGDirTxt))
        self.PNG2JPGQualitySlider.valueChanged.connect(lambda v: self.PNG2JPGQualityNum.setText(str(v)))
        # 图像序列转PDF信号
        self.Seq2PDFRun.clicked.connect(self.img2pdf_run)
        self.Seq2PDFStop.clicked.connect(lambda: worker_manager.request_stop())
        self.Seq2PDFPathOpen.clicked.connect(lambda: ui_utils.select_folder(self, self.Seq2PDFPathInput))

    def png2jpg_run(self):
        if worker_manager.is_busy():
            ui_utils.show_message_box(self, "提示", ErrorCode.WorkerBusy.generic, QMessageBox.Icon.Warning)
            return
        self.PNG2JPGRun.setEnabled(False)
        self.PNG2JPGStop.setEnabled(True)
        worker = PNG2JPGWorker(
            image_dir=self.PNG2JPGDirTxt.text(),
            recursive=self.PNG2JPGWalk.isChecked(),
            quality=self.PNG2JPGQualitySlider.value(),
            skip_transparency=self.PNG2JPGSkipAlpha.isChecked(),
            preserve_metadata=self.PNG2JPGPreverveMeta.isChecked(),
            delete_origin=self.PNG2JPGDelOri.isChecked(),
            conflict_mode=app_config.get_conflict_mode()
        )
        # 连接到主线程 QObject 的绑定方法，保证回调在主线程执行（详见 WorkerManager.submit 文档）
        worker.progress_updated.connect(self.PNG2JPGProgress.setValue)
        worker.worker_finished.connect(self.on_png2jpg_finished)
        if not worker_manager.submit(worker):
            self.PNG2JPGRun.setEnabled(True)
            self.PNG2JPGStop.setEnabled(False)

    def on_png2jpg_finished(self, result: tuple):
        self.PNG2JPGRun.setEnabled(True)
        self.PNG2JPGStop.setEnabled(False)
        ui_utils.show_message_box(self, result[0], result[1], result[2])

    def img2pdf_run(self):
        if worker_manager.is_busy():
            ui_utils.show_message_box(self, "提示", ErrorCode.WorkerBusy.generic, QMessageBox.Icon.Warning)
            return
        self.Seq2PDFRun.setEnabled(False)
        self.Seq2PDFStop.setEnabled(True)
        worker = ImgSeq2PDFWorker(
            folder=self.Seq2PDFPathInput.text(),
            recursive=self.Seq2PDFRecursive.isChecked(),
            send2trash=self.Seq2PDFDel.isChecked(),
            conflict_mode=app_config.get_conflict_mode()
        )
        # 连接到主线程 QObject 的绑定方法，保证回调在主线程执行（详见 WorkerManager.submit 文档）
        worker.progress_updated.connect(self.Seq2PDFProgress.setValue)
        worker.worker_finished.connect(self.on_img2pdf_finished)
        if not worker_manager.submit(worker):
            self.Seq2PDFRun.setEnabled(True)
            self.Seq2PDFStop.setEnabled(False)

    def on_img2pdf_finished(self, result: tuple):
        self.Seq2PDFRun.setEnabled(True)
        self.Seq2PDFStop.setEnabled(False)
        ui_utils.show_message_box(self, result[0], result[1], result[2])
