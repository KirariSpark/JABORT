import os

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMessageBox

from .worker_base import WorkerBase
from core.error_codes import ErrorCode
from core.logger import logger
from modules.conv import ImgSeq2PDF
from modules.utils.file_saver import FileConflictMode


class ImgSeq2PDFWorker(WorkerBase):
    progress_updated = Signal(int)

    def __init__(self, folder: str, send2trash: bool, recursive: bool,
                 conflict_mode: FileConflictMode = FileConflictMode.AddIndex):
        super().__init__()
        self.folder = folder
        self.send2trash = send2trash
        self.recursive = recursive
        self.conflict_mode = conflict_mode

    def task(self):
        logger.info(
            f"开始图像序列转PDF任务，目标路径: {self.folder}, 递归: {self.recursive}, 清理原文件: {self.send2trash}")

        if not self.folder or not os.path.isdir(self.folder):
            logger.error(ErrorCode.InvalidPath.format(self.folder))
            self.finish("错误", ErrorCode.InvalidPath.format(self.folder), QMessageBox.Icon.Critical)
            return

        try:
            results = ImgSeq2PDF.process_image_sequences(
                target_folder=self.folder,
                send_to_trash=self.send2trash,
                recursive=self.recursive,
                mode=self.conflict_mode
            )

            for res in results:
                if self._stop:
                    logger.info(ErrorCode.UserInterrupt.format("图像序列转PDF"))
                    self.finish("提示", ErrorCode.UserInterrupt.format("图像序列转PDF"),
                                QMessageBox.Icon.Information)
                    return
                elif res[0] != ErrorCode.Success:
                    logger.error(ErrorCode.Unknown.generic)
                    self.finish("错误", res[0].generic, QMessageBox.Icon.Information)
                    return
                else:
                    self.progress_updated.emit(res[1])

            # 循环正常结束
            logger.info(ErrorCode.Success.format("图像序列转PDF"))
            self.finish("完成", ErrorCode.Success.format("图像序列转PDF"), QMessageBox.Icon.Information)

        except Exception as e:
            logger.error(ErrorCode.Unknown.format(str(e)))
            self.finish("错误", ErrorCode.Unknown.format(str(e)), QMessageBox.Icon.Critical)
            return
