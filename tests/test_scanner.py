from typing import List
from unittest.mock import MagicMock, patch

from dubdub import Token
from dubdub.scanner import Scanner
from rich import print
from ward import test


@test("There's 4 tokens")
def test_ignorable():

    nested_scopes = "var hello = 1234.456"
    simple_scanner = Scanner(source=nested_scopes)
    assert simple_scanner.is_ignorable(" "), "The space isn't ignored"
    tokens: List[Token] = simple_scanner.scan_tokens()
    assert len(tokens) > 4, "There's an incorrect number of tokens. Should be 4 tokens."


@test("Recognized '==' and ; ending.")
def test_single_bracket():

    nested_scopes = "var hello == 1234.456;"
    simple_scanner = Scanner(source=nested_scopes)
    assert simple_scanner.is_ignorable(" "), "The space isn't ignored"
    tokens: List[Token] = simple_scanner.scan_tokens()
    assert len(tokens) > 0, "No tokens were extracted."


@test("Extract parentheses from number.")
def test_full_expression():
    parenthesis_expr = "(10 * 12 + (1 + 1))"
    scanner = Scanner(source=parenthesis_expr)
    tokens: List[Token] = scanner.scan_tokens()
    assert len(tokens) == 11
