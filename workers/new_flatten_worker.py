import os.path

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMessageBox

from .worker_base import WorkerBase
from core.error_codes import ErrorCode
from core.logger import logger
from modules.file_mgr import FlattenNew
from modules.utils.file_saver import FileConflictMode


class NewFlattenWorker(WorkerBase):
    progress_updated = Signal(int)

    def __init__(self, folder: str, conflict_mode: FileConflictMode = FileConflictMode.AddIndex):
        """
        展平一个文件夹（基于树的新实现）

        worker_finished 信号用于弹出提示框，第一项为标题，第二项为内容，第三项为图标

        Args:
            folder: 要展平的文件夹
            conflict_mode: 冲突处理模式
        """
        super().__init__()
        self.folder = folder
        self.conflict_mode = conflict_mode

    def task(self):
        if not self.folder or not os.path.exists(self.folder):
            logger.error("路径不存在或为空")
            self.finish("错误", "路径不存在或为空", QMessageBox.Icon.Critical)
            return

        try:
            logger.info(f"准备展平：{self.folder}")
            self.folder = os.path.normpath(self.folder)
            for stat, progress in FlattenNew.flatten(self.folder, self.conflict_mode):
                if self._stop:
                    logger.info("展平已被用户终止")
                    self.finish("信息", "展平已被终止", QMessageBox.Icon.Information)
                    return
                elif stat != ErrorCode.Success:
                    logger.error(stat.generic)
                    self.finish("错误", stat.generic, QMessageBox.Icon.Critical)
                    return
                else:
                    self.progress_updated.emit(int(progress * 0.9))
            logger.info(f"展平完成，准备清理")
            # 清理空文件夹
            stat = FlattenNew.cleanup(self.folder)
            if stat != ErrorCode.Success:
                logger.error(stat.generic)
                self.finish("错误", stat.generic, QMessageBox.Icon.Critical)
                return
            else:
                logger.info("清理完成")
                self.progress_updated.emit(100)
                self.finish("信息", "展平完成", QMessageBox.Icon.Information)
                return
        except Exception as e:
            logger.error(f"无法完成展平：{e}")
            self.finish("错误", f"无法完成展平：{e}", QMessageBox.Icon.Critical)
            return
