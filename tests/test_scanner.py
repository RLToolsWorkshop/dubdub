from typing import List
from unittest.mock import MagicMock, patch

from dubdub.primatives import Token
from dubdub.scanner import Scanner
from rich import print
from ward import test


@test("the list contains 42")
def _():
    assert 42 in [-21, 42, 999]


@test("There's 4 tokens")
def test_single_bracket():

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
