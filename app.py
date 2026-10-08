import os

import send2trash
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

from core import app_config
from modules.utils import ui_utils
from ui_app import Ui_Form

with open(r"styles\Blue Archive.qss", "r", encoding="utf-8") as f:
    stylesheet = f.read()


# UI
class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(stylesheet)
        self.ThemeDropdown.addItems([os.path.join("styles", item) for item in os.listdir("styles")])

        # 设置页面信号
        self.ThemeConfirm.clicked.connect(self.set_stylesheet)
        self.ClearLog.clicked.connect(self.clear_log)
        # 冲突处理模式：先按持久化值初始化，再连接信号
        self.FileConflictCombo.set_current_mode(app_config.get_conflict_mode())
        self.FileConflictCombo.currentIndexChanged.connect(self.save_conflict_mode)

    # 在当前线程运行的函数
    def set_stylesheet(self):
        with open(self.ThemeDropdown.currentText(), "r", encoding="utf-8") as style:
            style = style.read()
        self.setStyleSheet(style)

    def clear_log(self):
        try:
            logs = [os.path.join("logs", file) for file in os.listdir("logs") if file.endswith(".zip")]
            if logs:
                send2trash.send2trash(logs)
                ui_utils.show_message_box(self, "成功", "日志文件已删除", QMessageBox.Icon.Information)
            else:
                ui_utils.show_message_box(self, "错误", "没有日志文件", QMessageBox.Icon.Warning)
        except Exception as e:
            ui_utils.show_message_box(self, "错误", f"无法删除日志：{e}", QMessageBox.Icon.Critical)

    def save_conflict_mode(self):
        app_config.set_conflict_mode(self.FileConflictCombo.current_mode())


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()