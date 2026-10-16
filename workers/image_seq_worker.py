from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMessageBox

from .worker_base import WorkerBase
from modules.tests import ImgSeqGen
from core.error_codes import ErrorCode
from core.logger import logger


class ImageSeqWorker(WorkerBase):
    progress_updated = Signal(int)

    def __init__(self, num_images, output_folder):
        super().__init__()
        self.num_images = num_images
        self.output_folder = output_folder

    def task(self):
        if not self.output_folder:
            logger.error(ErrorCode.InvalidPath.format(self.output_folder))
            self.finish("错误", ErrorCode.InvalidPath.format(self.output_folder),
                        QMessageBox.Icon.Critical)
            return

        logger.info(f"开始生成 {self.num_images} 张图片到 {self.output_folder}")

        res = ImgSeqGen.generate_image_sequence(self.output_folder, self.num_images, (256, 256))

        for i in res:
            if self._stop:
                logger.info(ErrorCode.UserInterrupt.format("图像序列生成"))
                self.finish("提示", ErrorCode.UserInterrupt.format("图像序列生成"),
                            QMessageBox.Icon.Information)
                return

            self.progress_updated.emit(i[1])

            if i[0] != ErrorCode.Success:
                logger.error(i[0].generic)
                self.finish("错误", i[0].generic, QMessageBox.Icon.Critical)
                return

        logger.info(ErrorCode.Success.format("图像序列生成"))
        self.finish("完成", ErrorCode.Success.format("图像序列生成"), QMessageBox.Icon.Information)
