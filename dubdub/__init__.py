from loguru import logger
from pydantic import Field

from ._help import GenConfig, dataclass

__version__ = "0.1.0"


def error(line: int, message: str):
    logger.error(f"[line {line}] Error: {message}")
