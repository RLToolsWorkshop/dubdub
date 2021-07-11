import abc
from ast import Dict
from dataclasses import field
from datetime import datetime
from pathlib import Path
from typing import Any, List

from auto_all import end_all, start_all

from dubdub import dataclass
from dubdub.nodes import Node, Token
from dubdub.types import TokenType

CWD_DIR = Path.cwd()

start_all(globals())


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


@dataclass
class Assign(Stmt):
    """
    A way to access the variables.

    Args:
        Stmt ([type]): [description]
    """

    name: Token
    value: Expr


@dataclass
class Block(Stmt):
    stmts: List[Stmt] = field(default_factory=[])


@dataclass
class If(Stmt):
    condition: Expr
    then_branch: Stmt
    else_branch: Stmt


@dataclass
class While(Stmt):
    condition: Expr
    body: Stmt


@dataclass
class Call(Stmt):
    callee: Expr
    paren: Token
    arguments: List[Expr] = field(default_factory=[])


@dataclass
class Return(Stmt):
    keyword: Token
    value: Expr


@dataclass
class Logical(Expr):
    left: Expr
    right: Expr
    token: Token


class ReturnErr(RuntimeError):
    def __init__(self, value: Any, *args: object) -> None:
        super().__init__(*args)
        self.value = value


end_all(globals())


# @dataclass
# class Callable(Stmt):
#     callee: Expr
#     paren: Token
#     arguments: Expr


if __name__ == "__main__":
    test_binary = Binary(
        right=Unary(token=Token(TokenType.MINUS, "-", None, 1), right=Literal(123)),
        token=Token(TokenType.STAR, "*", None, 1),
        left=Grouping(Literal(45.67)),
    )

    print(test_binary)
