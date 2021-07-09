from typing import Optional

from dubdub import Token
from dubdub.types import TokenType


class ParserError(Exception):
    def __init__(self, token: Token, message: str, lexeme: Optional[str] = None):
        self.token = token
        self.message = message

    def __str__(self):
        if not self.token.token_type == TokenType.EOF:

            return f"{self.token.line} at '{self.token.lexeme}' {self.message}"
        return f"{self.token.line} at end {self.message}"
