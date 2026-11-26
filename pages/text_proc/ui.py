import os

from PySide6.QtWidgets import QWidget, QMessageBox

from modules.text_proc import JsonSorter, CalSimilarity, CropText, Moss
from modules.utils import ui_utils
from pages.text_proc.ui_page import Ui_TextProcWidget
from core import app_config
from core.error_codes import ErrorCode


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

        # MOSS 标签页
        self.MossDoParse.clicked.connect(self.moss_do_parse)
        self.MossSavePathOpen.clicked.connect(lambda: ui_utils.select_savefile(
            self, self.MossSavePath, "SRT 字幕 (*.srt)", self.MossSavePath.text()
        ))
        self.MossSaveCheck.toggled.connect(self.set_moss_save_enabled)
        self.set_moss_save_enabled(self.MossSaveCheck.isChecked())
        self.MossSpeakerCheck.setChecked(True)
        self.MossSpeakerCheck.toggled.connect(self.moss_speaker_toggled)
        self.MossHelp.clicked.connect(self.moss_help)

    def crop_text_run(self):
        res = CropText.crop_text_file(
            input_path=self.CropTextInPath.text(),
            output_path=self.CropTextOutPath.text(),
            percentage=self.CropTextRatioSpinbox.value(),
            mode=app_config.get_conflict_mode()
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

    def set_moss_save_enabled(self, enabled: bool):
        self.MossSavePath.setEnabled(enabled)
        self.MossSavePathOpen.setEnabled(enabled)

    def moss_speaker_toggled(self, checked: bool):
        text = self.MossTextInput.toPlainText()
        if not text.strip():
            return
        err, srt = Moss.convert(text, include_speaker=checked)
        if err is ErrorCode.Success:
            self.MossTextOutput.setPlainText(srt)

    def moss_help(self):
        ui_utils.show_message_box(
            self, "帮助",
            "将 MOSS Transcribe Diarize 输出的结构化文本转换为 SRT 字幕。\n\n"
            "输入格式：[开始时间][说话人]内容[结束时间]，时间单位为秒。\n\n"
            "勾选“包含说话人”会在字幕内容前保留说话人名称；\n"
            "勾选“保存到文件”并选择保存位置后，转换结果会同时写入 SRT 文件。",
            QMessageBox.Icon.Information
        )

    def moss_do_parse(self):
        output_path = self.MossSavePath.text().strip() if self.MossSaveCheck.isChecked() else None
        res = Moss.process(
            text=self.MossTextInput.toPlainText(),
            output_path=output_path,
            mode=app_config.get_conflict_mode(),
            include_speaker=self.MossSpeakerCheck.isChecked()
        )
        err, srt, saved_path = res
        self.MossTextOutput.setPlainText(srt)

        if err is ErrorCode.FileSkipped:
            ui_utils.show_message_box(self, "提示", err.generic, QMessageBox.Icon.Information)
        elif err.code:
            ui_utils.show_message_box(self, "错误", err.generic, QMessageBox.Icon.Critical)
        elif saved_path:
            ui_utils.show_message_box(self, "成功", f"转换完成，已保存到 {saved_path}",
                                      QMessageBox.Icon.Information)
        else:
            ui_utils.show_message_box(self, "成功", "转换完成", QMessageBox.Icon.Information)