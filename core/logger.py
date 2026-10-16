# -*- coding: utf-8 -*-
"""全局日志入口：初始化 KSEssentials 的 KSLogger，并导出 loguru 的全局 logger。

本模块在首次 import 时完成初始化；Python 的模块缓存保证重复 import 不会重复
添加 sink。任何模块只需 ``from core.logger import logger`` 即可直接使用。
"""
from loguru import logger  # noqa: F401  # 对外导出，供各模块使用

from KSEssentials.KSEnums import LogLevels
from KSEssentials.KSLogger import init_logger

# 与旧实现一致：等级为 INFO，写入 ./logs/latest.log，并自动归档上一份日志。
init_logger(level=LogLevels.Info)

__all__ = ["logger"]
