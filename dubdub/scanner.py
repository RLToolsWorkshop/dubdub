from dataclasses import field
from typing import Any, Dict, List, Optional, Tuple

from loguru import logger
from plum import dispatch

import dubdub
from dubdub import Field, GenConfig, dataclass
from dubdub.primatives import KEYWORDS, Token, TokenType


@dataclass(config=GenConfig)
class Scanner:
    source: str
    tokens: List[Token] = field(default_factory=lambda: [])

    # Scanner/Lexer Tracker
    start: int = 0
    current: int = 0
    line: int = 1

    src_len: int = 0

    # Variable to determine if we should move the start cursor on update
    is_jump: bool = False

    def __post_init__(self):
        self.src_len = len(self.source)

    @property
    def next_curr(self) -> int:
        return self.current + 1

    @property
    def idx_len(self) -> int:
        return self.src_len - 1

    def inc(self) -> int:
        """
        Increments the current cursor .
        """
        self.current += 1
        return self.current

    def log_idx(self):
        print("-------------------")
        logger.opt(depth=1).debug(
            f"\nCurrent: {self.current}\nStart: {self.start}\nSrc Length: {len(self.source)}\nTokens: {self.tokens}"
        )

    def is_end(self) -> bool:
        """
        Return True iff the source is at the end of the source file .

        Returns:
            bool: If end of source file.
        """
        return self.current >= self.idx_len

    def advance(self) -> str:
        """
        Return the next character in the source sequence .

        Returns:
            str: The next character
        """

        return self.source[min(self.inc(), self.idx_len)]

    @dispatch
    def add_token(self, token_type: TokenType):
        """
        Add a token to the token list .

        Args:
            token_type (TokenType): The token type.
        """
        self.add_token(token_type, None)

    @dispatch
    def add_token(self, token_type: TokenType, literal: Any):
        """
        Add a token to the source with literal.

        Args:
            token_type (TokenType): The TokenType Enum
            literal (Any): The literal text
        """
        lexeme_val: str = self.source[self.start : self.next_curr]
        self.tokens.append(
            Token(
                token_type=token_type,
                lexeme=lexeme_val,
                literal=literal,
                line=self.line,
            )
        )

    def match(self, expected: str) -> bool:
        """
        Check to see if the next item matches the expected value.
        Increments the the index by 1 if it does match.
        Args:
            expected (str): Expected char value.

        Returns:
            bool: True if it matches the expected value
        """
        if self.is_end():
            return False
        if self.source[self.next_curr] != expected:
            return False

        self.inc()
        return True

    def is_digit(self, c: str) -> bool:
        """
        Return True if c is a valid digit of the string .

        Args:
            c (str): [description]

        Returns:
            bool: True if it's a digit
        """
        return c.isdigit()

    def peek(self) -> str:
        """
        Returns the next character in the source string. Should be in the current cursor.

        Returns:
            str: The current char or an end code.
        """
        if self.is_end():
            return "\0"
        return self.source[self.current]

    def peek_next(self):
        if (self.current + 1) >= len(self.source):
            return "\0"
        return self.source[self.current + 1]


class _Scanner(Scanner):
    def single_token(self, char: str) -> bool:
        """Checks for and adds a single token.

        Args:
            char (str): the token at the current cursor

        Returns:
            bool: Returns true if we added a token in this function.
        """
        single_chars = {
            "(": TokenType.LEFT_PAREN,
            ")": TokenType.RIGHT_PAREN,
            "{": TokenType.LEFT_BRACE,
            "}": TokenType.RIGHT_BRACE,
            ",": TokenType.COMMA,
            ".": TokenType.DOT,
            "-": TokenType.MINUS,
            "+": TokenType.PLUS,
            ";": TokenType.SEMICOLON,
            "*": TokenType.STAR,
        }
        if char not in single_chars:
            return False

        token_type = single_chars.get(char)
        self.add_token(token_type)
        return True

    def double_token(self, char: str) -> bool:
        """
        Match double tokens. Tokens that can have an accompanied one.

        Args:
            char (str): the token at the current cursor
        """
        double_chars = {
            "!": ("=", TokenType.BANG_EQUAL, TokenType.BANG),
            "=": ("=", TokenType.EQUAL_EQUAL, TokenType.EQUAL),
            "<": ("=", TokenType.LESS_EQUAL, TokenType.LESS),
            ">": ("=", TokenType.GREATER_EQUAL, TokenType.GREATER),
        }
        if char not in double_chars:
            return False

        double_check: Tuple[str, TokenType, TokenType] = double_chars.get(char)
        is_match = self.match(double_check[0])
        resp_type: Optional[TokenType] = double_check[2]
        if is_match:
            resp_type: TokenType = double_check[1]

        self.add_token(resp_type)

        return True

    def comment_token(self, char: str) -> bool:
        """
        Add a comment to the token. Checks to find a single line comment. Ends at the end of line.

        Args:
            char (str): Current char
        """
        comm_token: Dict[str, TokenType] = {"/": TokenType.SLASH}
        if char not in comm_token:
            return False

        if self.match("/"):
            while self.peek() != "\n" and (not self.is_end()):
                self.advance()
        else:
            self.add_token(TokenType.SLASH)

        return True

    def is_ignorable(self, char: str) -> bool:
        return char in [" ", "\r", "\t", " "]


class Scanner(_Scanner):
    def string_scan(self) -> None:
        # When you see this kind of while loop it's searching for something to close the open string.
        while self.peek() != '"' and (not self.is_end()):
            if self.peek() == "\n":
                self.line += 1
            self.advance()

        if self.is_end():
            dubdub.error(self.line, "Unterminated string.")
            return False

        self.advance()

        value = self.source[self.start + 1 : self.current - 1]
        self.add_token(TokenType.STRING, value)
        return True

    def number_scan(self):
        # It's scanning until we we're no longer at a digit.
        while self.is_digit(self.peek()):
            self.advance()

        # If the non-digit character we're at is a decimal we check to see if the next num is

        if self.peek() == "." and self.is_digit(self.peek_next()):
            self.advance()
            # Basically the last peek expression all over again.
            while self.peek_next().isdigit():
                self.advance()
        num_value: str = self.source[self.start : self.next_curr]
        self.add_token(TokenType.NUMBER, float(num_value))

    def identity_scan(self):
        # Keep scanning until we reach non-alphanum

        while self.peek_next().isalnum():
            self.advance()

        identifier: str = self.source[self.start : self.next_curr]
        token_type: Optional[TokenType] = KEYWORDS.get(identifier, None)

        # Replace the token type with the identifier type if it's not a key word
        if not token_type:
            token_type = TokenType.IDENTIFIER

        self.add_token(token_type)

    def scan_token(self):
        """
        Scans the token stream .
        """
        char: str = self.advance()

        # If any tokens were added to the set we exit this function.

        if self.is_ignorable(char):
            self.is_jump = True
            return
        elif self.comment_token(char):
            return
        elif self.single_token(char):
            return
        elif self.double_token(char):
            return

        elif char == '"':
            if self.string_scan():
                return
        else:
            if char.isdigit():
                self.number_scan()
            elif char.isalpha():
                self.identity_scan()
            else:
                dubdub.error(self.line, "Unexpected character.")

    def update_start(self):
        self.start = self.current
        if self.is_jump:
            self.start += 1
            self.is_jump = False

    def scan_tokens(self) -> List[Token]:
        """
        Return a list of tokens that are not in the current token .

        Returns:
            List[Token]: List of tokens
        """
        while not self.is_end():
            self.update_start()
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens


def step():
    from rich import print

    nested_scopes = "var hello = 1234.456"
    scanner = Scanner(source=nested_scopes)
    tokens: List[Token] = scanner.scan_tokens()
    print(tokens)


if __name__ == "__main__":
    step()
