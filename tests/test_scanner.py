from typing import List
from unittest.mock import MagicMock, patch

from dubdub import Token
from dubdub.scanner import Scanner
from rich import print
from ward import test


@test("Can assign expression in parentheses")
def test_parentheses_assign() -> None:
    parenthesis_expr = "var hello_world = (10 * 12 + (1 + 1 ) );"
    scanner = Scanner(source=parenthesis_expr)
    tokens: List[Token] = scanner.scan_tokens()
    assert len(tokens) > 0


for exprs, count in [
    ("var hello_world = (10 * 12 + (1 + 1 ) );", 16),
    ("print 2 + 1 ;", 6),
]:

    @test("Multiple expressions parse correctly")
    def test_correct_token_number(expression=exprs, exp_count=count) -> None:
        scanner = Scanner(source=exprs)
        tokens: List[Token] = scanner.scan_tokens()
        assert len(tokens) == count


# @test("There's 4 tokens")
# def test_ignorable():

#     nested_scopes = "var hello = 1234.456;"
#     simple_scanner = Scanner(source=nested_scopes)
#     assert simple_scanner.is_ignorable(" "), "The space isn't ignored"
#     tokens: List[Token] = simple_scanner.scan_tokens()
#     assert (
#         tokens[-3].literal == 1234.456
#     ), "The number assigned doesn't match the expected outcome."
#     assert len(tokens) > 4, "There's an incorrect number of tokens. Should be 4 tokens."


# @test("Recognized '==' and ; ending.")
# def test_single_bracket():

#     nested_scopes = "var hello == 1234.456;"
#     simple_scanner = Scanner(source=nested_scopes)
#     assert simple_scanner.is_ignorable(" "), "The space isn't ignored"
#     tokens: List[Token] = simple_scanner.scan_tokens()
#     assert len(tokens) > 0, "No tokens were extracted."


# @test("Extract parentheses from number.")
# def test_full_expression():
#     parenthesis_expr = "(10 * 12 + (1 + 1 ) )"
#     scanner = Scanner(source=parenthesis_expr)
#     tokens: List[Token] = scanner.scan_tokens()
#     assert len(tokens) == 12


# @test("Ensure we extract both numbers and parentheses")
# def test_close_parent_expression():
#     parenthesis_expr = "(10 * 12 + (1 + 1));"
#     scanner = Scanner(source=parenthesis_expr)
#     tokens: List[Token] = scanner.scan_tokens()
#     print(tokens)
#     assert len(tokens) > 0


# @test("Ensure we extract both numbers and parentheses")
# def test_assign_string():
#     parenthesis_expr = 'var hello = "world";'
#     scanner = Scanner(source=parenthesis_expr)
#     tokens: List[Token] = scanner.scan_tokens()
#     print(tokens)
#     assert len(tokens) > 0


# @test("Can print string")
# def test_print_string():
#     parenthesis_expr = 'print "world";'
#     scanner = Scanner(source=parenthesis_expr)
#     tokens: List[Token] = scanner.scan_tokens()
#     print(tokens)
#     assert len(tokens) > 0


# @test("Can assign expression in parentheses")
# def test_parentheses_assign():
#     parenthesis_expr = "var hello_world = (10 * 12 + (1 + 1 ) );"
#     scanner = Scanner(source=parenthesis_expr)
#     tokens: List[Token] = scanner.scan_tokens()
#     assert len(tokens) > 0


# for exprs, count in [
#     ("var hello_world = (10 * 12 + (1 + 1 ) );", 16),
#     ("print 2 + 1 ;", 6),
# ]:

#     @test("Multiple expressions parse correctly")
#     def test_correct_token_number(expression=exprs, exp_count=count):
#         scanner = Scanner(source=exprs)
#         tokens: List[Token] = scanner.scan_tokens()
#         assert len(tokens) == count
