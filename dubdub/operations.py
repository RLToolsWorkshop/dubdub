import abc
from ast import Dict
from datetime import datetime
from pathlib import Path
from typing import Any, List

from dubdub import dataclass
from dubdub.nodes import Node, Token
from dubdub.types import TokenType

CWD_DIR = Path.cwd()


@dataclass
class Expr(Node):
    pass


@dataclass
class Stmt(Node):
    pass


@dataclass
class Binary(Expr):
    left: Expr
    right: Expr
    token: Token


@dataclass
class Grouping(Expr):
    expression: Expr


@dataclass
class Literal(Expr):
    value: Any


@dataclass
class Unary(Expr):
    right: Expr
    token: Token


@dataclass
class ExpressionStmt(Stmt):
    expression: Expr


@dataclass
class Print(Stmt):
    expression: Expr


@dataclass
class Var(Stmt):
    name: Token
    initializer: Expr


@dataclass
class Variable(Stmt):
    """
    A way to access the variables.

    Args:
        Stmt ([type]): [description]
    """

    name: Token


__all__ = [
    "Expr",
    "Binary",
    "Grouping",
    "Literal",
    "Unary",
    "Print",
    "ExpressionStmt",
    "Stmt",
    "Var",
    "Variable"
]


if __name__ == "__main__":
    test_binary = Binary(
        right=Unary(token=Token(TokenType.MINUS, "-", None, 1), right=Literal(123)),
        token=Token(TokenType.STAR, "*", None, 1),
        left=Grouping(Literal(45.67)),
    )

    print(test_binary)
