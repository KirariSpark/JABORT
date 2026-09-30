import os

from PySide6.QtCore import QSettings

from modules.utils.file_saver import FileConflictMode

# 临时配置模块，后续将由完整的配置系统替代
_CONFIG_PATH = os.path.join("config", "app_config.ini")
os.makedirs(os.path.dirname(_CONFIG_PATH), exist_ok=True)
_SETTINGS = QSettings(_CONFIG_PATH, QSettings.Format.IniFormat)
_KEY = "file_conflict_mode"


def get_conflict_mode() -> FileConflictMode:
    """读取冲突处理模式；缺失或值无效时返回默认的 AddIndex"""
    try:
        return FileConflictMode(_SETTINGS.value(_KEY, FileConflictMode.AddIndex.value))
    except ValueError:
        return FileConflictMode.AddIndex


def set_conflict_mode(mode: FileConflictMode) -> None:
    """保存冲突处理模式"""
    _SETTINGS.setValue(_KEY, mode.value)
    _SETTINGS.sync()
