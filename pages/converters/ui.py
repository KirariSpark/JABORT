from PySide6.QtWidgets import QWidget

from Workers import ImgSeq2PDFWorker, PNG2JPGWorker
from pages.converters.ui_page import Ui_ConverterWidget
from modules.utils import ui_utils
from core import app_config

class ConverterWidget(QWidget, Ui_ConverterWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.png2jpg_worker = None
        self.seq2pdf_worker = None

        # PNG转JPG信号
        self.PNG2JPGRun.clicked.connect(self.png2jpg_run)
        self.PNG2JPGStop.clicked.connect(lambda: self.png2jpg_worker.stop())
        self.PNG2JPGFindDir.clicked.connect(lambda: ui_utils.select_folder(self, self.PNG2JPGDirTxt))
        self.PNG2JPGQualitySlider.valueChanged.connect(lambda v: self.PNG2JPGQualityNum.setText(str(v)))
        # 图像序列转PDF信号
        self.Seq2PDFRun.clicked.connect(self.img2pdf_run)
        self.Seq2PDFStop.clicked.connect(lambda: self.seq2pdf_worker.stop())
        self.Seq2PDFPathOpen.clicked.connect(lambda: ui_utils.select_folder(self, self.Seq2PDFPathInput))

    def png2jpg_run(self):
        self.PNG2JPGRun.setEnabled(False)
        self.PNG2JPGStop.setEnabled(True)
        self.png2jpg_worker = PNG2JPGWorker(
            image_dir=self.PNG2JPGDirTxt.text(),
            recursive=self.PNG2JPGWalk.isChecked(),
            quality=self.PNG2JPGQualitySlider.value(),
            skip_transparency=self.PNG2JPGSkipAlpha.isChecked(),
            preserve_metadata=self.PNG2JPGPreverveMeta.isChecked(),
            delete_origin=self.PNG2JPGDelOri.isChecked(),
            conflict_mode=app_config.get_conflict_mode()
        )
        self.png2jpg_worker.progress_updated.connect(lambda v: self.PNG2JPGProgress.setValue(int(v)))
        self.png2jpg_worker.worker_finished.connect(lambda: self.PNG2JPGRun.setEnabled(True))
        self.png2jpg_worker.worker_finished.connect(lambda: self.PNG2JPGStop.setEnabled(False))
        self.png2jpg_worker.worker_finished.connect(lambda t: ui_utils.show_message_box(self, t[0], t[1], t[2]))
        self.png2jpg_worker.start()

    def img2pdf_run(self):
        self.Seq2PDFRun.setEnabled(False)
        self.Seq2PDFStop.setEnabled(True)
        self.seq2pdf_worker = ImgSeq2PDFWorker(
            folder=self.Seq2PDFPathInput.text(),
            recursive=self.Seq2PDFRecursive.isChecked(),
            send2trash=self.Seq2PDFDel.isChecked(),
            conflict_mode=app_config.get_conflict_mode()
        )
        self.seq2pdf_worker.worker_finished.connect(lambda: self.Seq2PDFRun.setEnabled(True))
        self.seq2pdf_worker.worker_finished.connect(lambda: self.Seq2PDFStop.setEnabled(False))
        self.seq2pdf_worker.worker_finished.connect(lambda t: ui_utils.show_message_box(self, t[0], t[1], t[2]))
        self.seq2pdf_worker.progress_updated.connect(lambda v: self.Seq2PDFProgress.setValue(v))
        self.seq2pdf_worker.start()
