from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from loguru import logger

from dubdub import (
    Binary,
    Expr,
    Grouping,
    Literal,
    Node,
    Token,
    TokenType,
    Unary,
    Visitor,
)


class PrintVisitor(Visitor):
    # def on_visit(self, node: Node):
    #     logger.warning(f"Printing {node.vname}")
    #     return super().on_visit(node)

    def visit_token(self, node: "Node"):
        logger.debug("Visiting a token")

    def visit_binary(self, node: "Binary"):
        return self.parenthesize(node.token.lexeme, node.right, node.left)

    def visit_unary(self, node: "Node"):
        return self.parenthesize(node.token.lexeme, node.right)

    """
        Normal expressions 
    """

    def visit_grouping(self, expr: "Grouping") -> str:
        return self.parenthesize("group", expr.expression)

    def visit_literal(self, node: "Literal") -> str:
        if node.value is None:
            return "nil"
        return str(node.value)

    def parenthesize(self, name: str, *exprs: "Expr"):
        str_resp: str = f"({name}"
        for expr in exprs:
            expr_resp = self.visit(expr)
            str_resp += f" {expr_resp}"
        str_resp += f")"
        return str_resp


def step():
    test_binary = Binary(
        right=Unary(token=Token(TokenType.MINUS, "-", None, 1), right=Literal(123)),
        token=Token(TokenType.STAR, "*", None, 1),
        left=Grouping(Literal(45.67)),
    )
    printer = PrintVisitor()

    logger.info(printer.visit(test_binary))


if __name__ == "__main__":
    step()
