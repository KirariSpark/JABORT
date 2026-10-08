from PySide6.QtWidgets import QComboBox

from modules.utils.file_saver import FileConflictMode


class FileConflictCombo(QComboBox):
    """
    文件冲突处理模式下拉框

    展示「覆盖 / 跳过 / 增加序号」三个选项，
    对外返回对应的 FileConflictMode 枚举成员，而非字符串。
    """

    # 与下拉项顺序一致的模式列表
    _MODES = [
        FileConflictMode.Overwrite,
        FileConflictMode.Skip,
        FileConflictMode.AddIndex,
    ]

    def __init__(self, parent=None):
        super().__init__(parent)
        # 显示文本直接取枚举值
        self.addItems([mode.value for mode in self._MODES])
        self.set_current_mode(FileConflictMode.AddIndex)

    def current_mode(self) -> FileConflictMode:
        """返回当前选中的冲突处理模式"""
        index = self.currentIndex()
        if 0 <= index < len(self._MODES):
            return self._MODES[index]
        return FileConflictMode.AddIndex

    def set_current_mode(self, mode: FileConflictMode):
        """设置当前选中的冲突处理模式"""
        self.setCurrentIndex(self._MODES.index(mode))
