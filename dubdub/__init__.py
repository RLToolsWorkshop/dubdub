from loguru import logger
from pydantic import Field, create_model

from ._help import GenConfig, dataclass
from .nodes import Node, Token, Visitor
from .operations import Binary, Expr, Grouping, Literal, Unary

# isort:skip
from .types import TokenType

__version__ = "0.1.0"
KEYWORDS = {
    "and": TokenType.AND,
    "class": TokenType.CLASS,
    "else": TokenType.ELSE,
    "false": TokenType.FALSE,
    "for": TokenType.FOR,
    "fun": TokenType.FUN,
    "if": TokenType.IF,
    "nil": TokenType.NIL,
    "or": TokenType.OR,
    "print": TokenType.PRINT,
    "return": TokenType.RETURN,
    "super": TokenType.SUPER,
    "this": TokenType.THIS,
    "true": TokenType.TRUE,
    "var": TokenType.VAR,
    "while": TokenType.WHILE,
}


def error(line: int, message: str):
    logger.error(f"[line {line}] Error: {message}")
