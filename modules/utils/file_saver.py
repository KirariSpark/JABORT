import json
import os
import re
import shutil
from enum import Enum
from typing import Any, Callable

from core.error_codes import ErrorCode
from core.logger import logger


class FileConflictMode(Enum):
    """
    文件冲突处理模式

    枚举值同时用作界面展示文本，对外只接受枚举成员，不接受整数。
    """
    Overwrite = "重复的文件：覆盖"
    Skip = "重复的文件：跳过"
    AddIndex = "重复的文件：增加序号"


def get_unique_path(path: str) -> tuple[ErrorCode, str]:
    """
    获取唯一的文件路径，为重名的文件添加序号

    :param path: 要处理的路径
    :return: 元组，第一项为错误码，第二项为唯一文件路径
    """
    logger.debug(f"为 {path} 获取唯一的文件路径")
    dir_path = os.path.dirname(path) or '.'
    filename, ext = os.path.splitext(os.path.basename(path))

    # 文件不存在 - 没有重名
    if not os.path.exists(path):
        logger.debug("没有检测到重复文件")
        return ErrorCode.Success, path
    # 文件存在 - 有重名
    files = os.listdir(dir_path)
    pattern_str = f"^{re.escape(filename)}_(\\d+){re.escape(ext)}$"
    logger.debug(f"检测到重复文件，构建正则表达式：{pattern_str}")
    pattern = re.compile(pattern_str)

    indices = [int(match.group(1)) for f in files if (match := pattern.match(f))]
    logger.debug(f"检测到的序列：{indices}")
    max_index = max(indices, default=0)

    new_index = max_index + 1
    new_filename = f"{filename}_{new_index}{ext}"
    logger.debug(f"唯一文件名：{new_filename}")

    return ErrorCode.Success, os.path.join(dir_path, new_filename)


def resolve_conflict(path: str, mode: FileConflictMode) -> tuple[ErrorCode, str]:
    """
    根据冲突处理模式解析最终的文件路径

    Args:
        path: 目标文件路径
        mode: 冲突处理模式（FileConflictMode 枚举成员）

    Returns:
        元组，第一项为错误码，第二项为解析后的文件路径；
        跳过模式下文件已存在时返回 ErrorCode.FileSkipped
    """
    if not isinstance(mode, FileConflictMode):
        logger.error(f"无效的冲突处理模式：{mode!r}")
        return ErrorCode.InvalidArgument, path

    logger.debug(f"使用 {mode.value} 模式解析文件冲突：{path}")
    # 覆盖 - 直接使用原路径
    if mode is FileConflictMode.Overwrite:
        return ErrorCode.Success, path
    # 跳过 - 文件不存在则可用，存在则跳过
    elif mode is FileConflictMode.Skip:
        if os.path.exists(path):
            logger.info(ErrorCode.FileSkipped.format(path))
            return ErrorCode.FileSkipped, path
        return ErrorCode.Success, path
    # 增加序号 - 生成唯一路径
    else:
        return get_unique_path(path)


def save_with(path: str, writer: Callable[[str], Any],
              mode: FileConflictMode = FileConflictMode.AddIndex) -> tuple[ErrorCode, str]:
    """
    解析冲突后调用 writer 将内容写入最终路径

    适用于需要一个最终路径的回调场景（如 PIL 图像保存、PDF 保存等）。

    Args:
        path: 目标文件路径
        writer: 接收最终路径并执行写入的回调
        mode: 冲突处理模式

    Returns:
        元组，第一项为错误码，第二项为实际写入的文件路径
    """
    err, final_path = resolve_conflict(path, mode)
    # 冲突解析失败或命中跳过 - 不写盘
    if err is not ErrorCode.Success:
        return err, final_path

    try:
        writer(final_path)
    except PermissionError as e:
        logger.error(ErrorCode.NotPermitted.format(str(e)))
        return ErrorCode.NotPermitted, final_path
    except Exception as e:
        logger.error(ErrorCode.CannotWriteFile.format(str(e)))
        return ErrorCode.CannotWriteFile, final_path

    logger.info(f"已写入文件：{final_path}")
    return ErrorCode.Success, final_path


def save_bytes(path: str, data: bytes,
               mode: FileConflictMode = FileConflictMode.AddIndex) -> tuple[ErrorCode, str]:
    """
    将字节数据写入文件，并按模式处理重名冲突

    Args:
        path: 目标文件路径
        data: 要写入的字节数据
        mode: 冲突处理模式

    Returns:
        元组，第一项为错误码，第二项为实际写入的文件路径
    """
    def writer(final_path: str):
        with open(final_path, 'wb') as f:
            f.write(data)

    return save_with(path, writer, mode)


def save_text(path: str, data: str, mode: FileConflictMode = FileConflictMode.AddIndex,
              encoding: str = "utf-8") -> tuple[ErrorCode, str]:
    """
    将文本写入文件，并按模式处理重名冲突

    Args:
        path: 目标文件路径
        data: 要写入的文本
        mode: 冲突处理模式
        encoding: 文件编码

    Returns:
        元组，第一项为错误码，第二项为实际写入的文件路径
    """
    def writer(final_path: str):
        with open(final_path, 'w', encoding=encoding) as f:
            f.write(data)

    return save_with(path, writer, mode)


def save_json(path: str, data: Any, mode: FileConflictMode = FileConflictMode.AddIndex,
              encoding: str = "utf-8", indent: int | None = 4,
              ensure_ascii: bool = False) -> tuple[ErrorCode, str]:
    """
    将数据以 JSON 写入文件，并按模式处理重名冲突

    Args:
        path: 目标文件路径
        data: 要序列化的数据
        mode: 冲突处理模式
        encoding: 文件编码
        indent: JSON 缩进，None 表示不缩进
        ensure_ascii: 是否将非 ASCII 字符转义

    Returns:
        元组，第一项为错误码，第二项为实际写入的文件路径
    """
    def writer(final_path: str):
        with open(final_path, 'w', encoding=encoding) as f:
            json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)

    return save_with(path, writer, mode)


def build_output_path(input_path: str, prefix: str = "", suffix: str = "",
                      spacing: str = "", mode: FileConflictMode = FileConflictMode.AddIndex) -> tuple[ErrorCode, str]:
    """
    构建带前后缀的输出路径，并按模式处理重名冲突

    Args:
        input_path: 输入文件路径
        prefix: 追加到文件名前的前缀
        suffix: 追加到文件名后的后缀
        spacing: 前后缀与原文件名之间的填充字符
        mode: 冲突处理模式

    Returns:
        元组，第一项为错误码，第二项为输出文件路径
    """
    safe_prefix = prefix.replace('/', '').replace('\\', '')
    safe_suffix = suffix.replace('/', '').replace('\\', '')

    folder = os.path.dirname(input_path)
    name, ext = os.path.splitext(os.path.basename(input_path))
    name = f"{safe_prefix}{spacing if safe_prefix else ''}{name}{spacing if safe_suffix else ''}{safe_suffix}"
    output_path = os.path.join(folder, f"{name}{ext}")

    return resolve_conflict(output_path, mode)


def move_with(src: str, dst: str,
              mode: FileConflictMode = FileConflictMode.AddIndex) -> tuple[ErrorCode, str]:
    """
    按冲突模式解析目标路径后，将源文件/文件夹移动到目标路径

    Args:
        src: 源路径
        dst: 目标路径
        mode: 冲突处理模式

    Returns:
        元组，第一项为错误码，第二项为实际移动到的目标路径
    """
    err, final_path = resolve_conflict(dst, mode)
    # 冲突解析失败或命中跳过 - 不移动
    if err is not ErrorCode.Success:
        return err, final_path

    try:
        shutil.move(src, final_path)
    except PermissionError as e:
        logger.error(ErrorCode.NotPermitted.format(str(e)))
        return ErrorCode.NotPermitted, final_path
    except Exception as e:
        logger.error(ErrorCode.CannotWriteFile.format(str(e)))
        return ErrorCode.CannotWriteFile, final_path

    logger.info(f"已移动：{src} -> {final_path}")
    return ErrorCode.Success, final_path
