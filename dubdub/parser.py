from typing import List

from loguru import logger
from rich import print

from dubdub import Expr, Token, dataclass
from dubdub import errors as erx
from dubdub.errors import ParserError
from dubdub.operations import *
from dubdub.scanner import Scanner
from dubdub.types import TokenType


@dataclass
class Parser:
    tokens: List[Token]
    current: int = 0

    def peek(self) -> Token:
        return self.tokens[self.current]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    def is_end(self) -> bool:
        return self.peek().token_type == TokenType.EOF

    def advance(self) -> Token:
        if not self.is_end():
            self.current += 1
        return self.previous()

    def check(self, checking_type: TokenType) -> bool:
        if self.is_end():
            return False
        return self.peek().token_type == checking_type

    def match(self, *check_types: TokenType) -> bool:
        """Match one of the given types.


        Returns:
            args[TypeToken]: A list of token types
        """
        for _type in check_types:
            if self.check(_type):
                self.advance()
                return True

        return False

    def consume(self, token_type: TokenType, message: str) -> Token:
        if self.check(token_type):
            return self.advance()
        raise ParserError(self.peek(), "Expect ')' after expression.")


@dataclass
class __ParserGrammar(Parser):
    def expression(self):
        return self.equality()

    def equality(self) -> Expr:
        expr: Expr = self.comparison()

        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator: Token = self.previous()
            right: Expr = self.comparison()
            expr: Expr = Binary(left=expr, token=operator, right=right)

        return expr

    def comparison(self) -> Expr:
        expr: Expr = self.term()

        while self.match(
            TokenType.GREATER,
            TokenType.GREATER_EQUAL,
            TokenType.LESS,
            TokenType.LESS_EQUAL,
        ):
            operator: Token = self.previous()
            right: Expr = self.term()
            expr: Expr = Binary(left=expr, token=operator, right=right)

        return expr

    def term(self):
        expr: Expr = self.factor()

        while self.match(
            TokenType.MINUS,
            TokenType.PLUS,
        ):
            operator: Token = self.previous()
            right: Expr = self.factor()
            expr: Expr = Binary(left=expr, token=operator, right=right)

        return expr

    def factor(self):
        expr: Expr = self.unary()

        while self.match(
            TokenType.SLASH,
            TokenType.STAR,
        ):
            operator: Token = self.previous()
            right: Expr = self.unary()
            expr: Expr = Binary(left=expr, token=operator, right=right)

        return expr

    def unary(self):
        if self.match(
            TokenType.BANG,
            TokenType.MINUS,
        ):
            operator: Token = self.previous()
            right: Expr = self.primary()
            return Unary(token=operator, right=right)
        return self.primary()

    def primary(self):
        if self.match(TokenType.FALSE):
            return Literal(value=False)
        elif self.match(TokenType.TRUE):
            return Literal(value=True)
        elif self.match(TokenType.NIL):
            return Literal(value=None)
        elif self.match(TokenType.STRING, TokenType.NUMBER):
            return Literal(value=self.previous().literal)
        elif self.match(TokenType.LEFT_PAREN):
            expr: Expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Missing right parenthesis")
            return Grouping(expression=expr)

        raise ParserError(self.peek(), "Expected expression.")


@dataclass
class Parser(__ParserGrammar):
    def parse(self):
        try:
            return self.expression()
        except ParserError as pe:
            logger.exception(pe)
        except Exception as e:
            logger.exception(e)
            raise e


def main():
    # nested_scopes = "var hello = 1234.456;"
    nested_scopes = "( 10 * 12 + ( 1 + 1 ) )"
    scanner = Scanner(source=nested_scopes)
    tokens: List[Token] = scanner.scan_tokens()
    # print(tokens)
    parser = Parser(tokens=tokens)
    parsed = parser.parse()
    print(tokens)
    print(parsed)


if __name__ == "__main__":
    main()
