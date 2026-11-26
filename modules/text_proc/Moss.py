import os
import re
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from typing import Iterable

from core.error_codes import ErrorCode
from core.logger import logger
from modules.utils import file_saver
from modules.utils.file_saver import FileConflictMode

# 时间戳：单位为秒，允许整数或小数
_TIMESTAMP = r"\d+(?:\.\d+)?"
# 一个 MOSS 片段：[开始时间][说话人]内容[结束时间]
_SEGMENT_PATTERN = re.compile(
    rf"\[\s*(?P<start>{_TIMESTAMP})\s*\]"
    rf"\[\s*(?P<speaker>[^\[\]\r\n]+?)\s*\]"
    rf"(?P<content>.*?)"
    rf"\[\s*(?P<end>{_TIMESTAMP})\s*\]",
    re.DOTALL,
)


@dataclass(frozen=True)
class MossSegment:
    """MOSS 结构化文本中的一个片段"""
    start: Decimal
    speaker: str
    content: str
    end: Decimal


def parse_segments(text: str) -> list[MossSegment]:
    """
    解析 MOSS Transcribe Diarize 输出的结构化文本

    片段格式：[开始时间戳][说话人名称]具体内容[截止时间戳]
    时间戳单位为秒。

    Args:
        text: MOSS 原始文本

    Returns:
        解析出的片段列表；没有匹配到任何片段时返回空列表
    """
    segments = []
    for match in _SEGMENT_PATTERN.finditer(text):
        speaker = match.group("speaker").strip()
        if not speaker:
            logger.warning("跳过说话人为空的 MOSS 片段")
            continue
        segment = MossSegment(
            start=Decimal(match.group("start")),
            speaker=speaker,
            content=match.group("content").strip(),
            end=Decimal(match.group("end")),
        )
        logger.debug(f"解析到片段：{segment}")
        segments.append(segment)
    return segments


def seconds_to_srt_timestamp(seconds: Decimal) -> str:
    """
    将秒转换为 SRT 时间戳（HH:MM:SS,mmm）

    Args:
        seconds: 秒数

    Returns:
        SRT 格式的时间戳
    """
    total_ms = int((seconds * 1000).to_integral_value(rounding=ROUND_HALF_UP))
    hours, remainder = divmod(total_ms, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, milliseconds = divmod(remainder, 1_000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"


def segments_to_srt(segments: Iterable[MossSegment], include_speaker: bool = True) -> str:
    """
    将片段列表转换为 SRT 文本

    Args:
        segments: 片段列表
        include_speaker: 是否在字幕内容前保留说话人名称

    Returns:
        SRT 文本
    """
    blocks = []
    for index, segment in enumerate(segments, start=1):
        start = seconds_to_srt_timestamp(segment.start)
        end = seconds_to_srt_timestamp(segment.end)
        content = f"{segment.speaker}：{segment.content}" if include_speaker else segment.content
        blocks.append(
            f"{index}\n"
            f"{start} --> {end}\n"
            f"{content}\n"
        )
    return "\n".join(blocks)


def convert(text: str, include_speaker: bool = True) -> tuple[ErrorCode, str]:
    """
    将 MOSS 结构化文本转换为 SRT 文本

    Args:
        text: MOSS 原始文本
        include_speaker: 是否在字幕内容前保留说话人名称

    Returns:
        元组，第一项为错误码，第二项为 SRT 文本（失败时为空字符串）
    """
    logger.info("正在将 MOSS 文本转换为 SRT")
    if not text or not text.strip():
        logger.error(ErrorCode.EmptyString)
        return ErrorCode.EmptyString, ""

    segments = parse_segments(text)
    if not segments:
        logger.error(ErrorCode.InvalidFormat.format("未找到符合 MOSS 格式的片段"))
        return ErrorCode.InvalidFormat, ""

    srt = segments_to_srt(segments, include_speaker=include_speaker)
    logger.info(f"已转换 {len(segments)} 个片段")
    return ErrorCode.Success, srt


def save_srt(srt_text: str, output_path: str,
             mode: FileConflictMode = FileConflictMode.AddIndex) -> tuple[ErrorCode, str]:
    """
    将 SRT 文本保存到文件

    Args:
        srt_text: SRT 文本
        output_path: 输出文件路径
        mode: 冲突处理模式

    Returns:
        元组，第一项为错误码，第二项为实际保存的文件路径
    """
    if not output_path:
        logger.error(ErrorCode.InvalidPath.format(output_path))
        return ErrorCode.InvalidPath, ""
    output_dir = os.path.dirname(os.path.abspath(output_path))
    if not os.path.isdir(output_dir):
        logger.error(ErrorCode.InvalidPath.format(output_dir))
        return ErrorCode.InvalidPath, ""

    res = file_saver.save_text(output_path, srt_text, mode)
    if res[0] is ErrorCode.Success:
        logger.info(f"已将 SRT 保存到 {res[1]}")
    return res


def process(text: str, output_path: str | None = None,
            mode: FileConflictMode = FileConflictMode.AddIndex,
            include_speaker: bool = True) -> tuple[ErrorCode, str, str]:
    """
    转换 MOSS 文本，并按需保存为 SRT

    Args:
        text: MOSS 原始文本
        output_path: 输出文件路径；为 None 时不保存，为空字符串时视为无效路径
        mode: 冲突处理模式
        include_speaker: 是否在字幕内容前保留说话人名称

    Returns:
        元组，第一项为错误码，第二项为 SRT 文本，第三项为实际保存的文件路径
    """
    err, srt = convert(text, include_speaker=include_speaker)
    if err is not ErrorCode.Success:
        return err, "", ""
    if output_path is None:
        return ErrorCode.Success, srt, ""

    err, saved_path = save_srt(srt, output_path, mode)
    return err, srt, saved_path


def main(text: str, include_speaker: bool = True) -> tuple[ErrorCode, str]:
    """MOSS 转换入口，等同于 convert"""
    return convert(text, include_speaker=include_speaker)
