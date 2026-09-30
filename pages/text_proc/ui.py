import os

from PySide6.QtWidgets import QWidget, QMessageBox

from modules.text_proc import JsonSorter, CalSimilarity, CropText
from modules.utils import ui_utils
from pages.text_proc.ui_page import Ui_TextProcWidget


class TextProcWidget(QWidget, Ui_TextProcWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.CropTextInPathOpen.clicked.connect(lambda: ui_utils.select_file(self, self.CropTextInPath))
        self.CropTextOutPathOpen.clicked.connect(lambda: ui_utils.select_savefile(self, self.CropTextOutPath))
        self.CroptextRun.clicked.connect(self.crop_text_run)
        self.CalSimModelRefresh.clicked.connect(lambda: ui_utils.refresh_combobox(
            target_widget=self.CalSimModelDropdown, path="resources/models/embeddings", include_path=False, parent=self
        ))
        self.CalSimUnload.clicked.connect(lambda: ui_utils.show_message_box(
            self, content=CalSimilarity.unload_model(), icon=QMessageBox.Icon.Information
        ))
        self.JsonSorterInOpen.clicked.connect(lambda: ui_utils.select_file(
            self, self.JsonSorterInPath, "*.json"
        ))
        self.JsonSorterRun.clicked.connect(self.json_sorter_run)

    def crop_text_run(self):
        res = CropText.crop_text_file(
            input_path=self.CropTextInPath.text(),
            output_path=self.CropTextOutPath.text(),
            percentage=self.CropTextRatioSpinbox.value(),
            deduplicate=self.CropTextDedup.currentIndex()
        )
        if res[0].code:
            ui_utils.show_message_box(self, "错误", res[0].generic, QMessageBox.Icon.Critical)
        else:
            ui_utils.show_message_box(self, "成功", f"裁剪后的文本已保存到 {res[1]}",
                                      QMessageBox.Icon.Information)

    def cal_similarity_run(self):
        res = CalSimilarity.main(
            str1=self.CalSimIn1.text(), str2=self.CalSimIn2.text(),
            model=os.path.join("resources", "models", "embeddings", self.CalSimModelDropdown.currentText()),
            persistent_model=self.CalSimPersistentModel.isChecked()
        )
        if res[0].code:
            ui_utils.show_message_box(self, "错误", res[0].generic, QMessageBox.Icon.Critical)
        else:
            ui_utils.show_message_box(self, "计算结果", f"输入内容的相似度为 {res[1]}",
                                      QMessageBox.Icon.Information)

    def json_sorter_run(self):
        res = JsonSorter.main(self.JsonSorterInPath.text())
        if res[0]:
            ui_utils.show_message_box(self, "错误", res[1], QMessageBox.Icon.Critical)
        else:
            ui_utils.show_message_box(self, "信息", "排序已完成，结果已保存到原文件",
                                      QMessageBox.Icon.Information)