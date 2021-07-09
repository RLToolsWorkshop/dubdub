import abc
from ast import Dict
from datetime import datetime
from pathlib import Path
from typing import Any, List

from loguru import logger
from rich import print

from dubdub import (
    Binary,
    Grouping,
    Literal,
    Node,
    Token,
    TokenType,
    Unary,
    Visitor,
    dataclass,
)
from dubdub.operations import ExpressionStmt, Print, Stmt
from dubdub.parser import Parser
from dubdub.scanner import Scanner

CWD_DIR = Path.cwd()


@dataclass
class Intepreter(Visitor):
    def is_truthy(self, value: Any) -> bool:
        if value is None:
            return False

        if isinstance(value, bool):
            return value

        return True

    def is_equal(self, first: Any, second: Any) -> bool:
        return first == second

    def visit_binary(self, expr: "Binary"):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)
        token_type = expr.token.token_type

        if TokenType.GREATER:
            return float(left) > float(right)
        elif TokenType.GREATER_EQUAL:
            return float(left) >= float(right)
        elif TokenType.LESS:
            return float(left) < float(right)
        elif TokenType.LESS_EQUAL:
            return float(left) <= float(right)
        elif TokenType.BANG_EQUAL:
            return self.is_equal(left, right)
        elif token_type == TokenType.MINUS:
            return float(left) - float(right)
        elif token_type == TokenType.SLASH:
            return float(left) / float(right)
        elif token_type == TokenType.STAR:
            return float(left) * float(right)
        elif token_type == TokenType.PLUS:
            if isinstance(left, str) and isinstance(right, str):
                return str(left) + str(right)
            elif isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return float(left) + float(right)
            raise TypeError("One of the two evaluated expressions is off.")

    def visit_unary(self, node: "Unary"):
        right = self.evaluate(node.right)
        exp_types = {
            TokenType.MINUS: lambda x: (-1 * x),
            TokenType.BANG: lambda x: (not self.is_truthy(x)),
        }
        resp_fn = exp_types.get(node.token.token_type, None)
        if resp_fn is not None:
            return resp_fn(right)
        raise Exception("Shouldn't have touched this here.")

    """
        Normal expressions 
    """

    def visit_grouping(self, expr: "Grouping") -> str:
        return self.evaluate(expr.expression)

    def visit_literal(self, node: "Literal") -> Any:
        return node.value

    def visit_token(self, node: "Token"):
        logger.debug("Visiting a token")

    def visit_expression_stmt(self, stmt: ExpressionStmt):
        return self.evaluate(stmt.expression)

    def visit_print(self, print_stmt: Print):
        value = self.evaluate(print_stmt.expression)
        print(str(value))

    def evaluate(self, node: "Node") -> Any:
        return self.visit(node)

    def intepret(self, statements: List[Stmt]):
        for stmt in statements:
            self.evaluate(stmt)


def main():
    # nested_scopes = "var hello = 1234.456;"
    # Note: The scanner has a index bug. Will need to solve it at some point.
    # nested_scopes = " 10 * 12 + ( 1 + 1 ) "
    nested_scopes = "( 100 == 100 )"
    scanner = Scanner(source=nested_scopes)
    tokens: List[Token] = scanner.scan_tokens()
    print(tokens)

    parser = Parser(tokens=tokens)
    parsed_stmts = parser.parse()

    interp = Intepreter()
    print(parsed_stmts)

    # resp = interp.intepret(parsed_stmts)
    # print(resp)


if __name__ == "__main__":
    main()
