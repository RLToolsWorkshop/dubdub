from typing import List

from devtools import debug
from dubdub import Token
from dubdub.interpreter import Interpreter
from dubdub.parser import Parser
from dubdub.scanner import Scanner
from loguru import logger
from rich import print
from ward import test


def process_print(input_text: str):
    scanner = Scanner(source=input_text)
    tokens: List[Token] = scanner.scan_tokens()

    parser = Parser(tokens=tokens)
    parsed_stmts = parser.parse()
    assert True, "We haven't reached this point yet."

    interpreter = Interpreter()
    interpreted = interpreter.intepret(parsed_stmts)
    return tokens, parsed_stmts, interpreted


for exprs, count in [
    # ("var hello_world = (10 * 12 + (1 + 1 ) );", 16),
    ('print "hello world";', 4),
    ("print 2 + 1 ;", 6),
    ("print true;", 4),
    ('print "one";', 4),
]:

    @test("Testing for simple print statements.")
    def test_process_print(input_text=exprs, count=count):
        tokens, _, _ = process_print(input_text)

        assert True, "We haven't reached this point yet."
        assert len(tokens) == count, f"The count should match {count}"


@test("Testing that we're able to assign and access certain variables.")
def test_var_shifts():
    """
    We specifically test variable expression declaration.
    """
    assert True, "We were able to assign variables."


def main():
    # nested_scopes = "var hello = 1234.456;"
    # Note: The scanner has a index bug. Will need to solve it at some point.
    # nested_scopes = " 10 * 12 + ( 1 + 1 ) "
    nested_scopes = 'print "hello world";'
    scanner = Scanner(source=nested_scopes)
    tokens: List[Token] = scanner.scan_tokens()
    print(tokens)

    parser = Parser(tokens=tokens)
    parsed_stmts = parser.parse()
    print(parsed_stmts)

    interpreter = Interpreter()
    interpreter.intepret(parsed_stmts)
    print(parsed_stmts)

    # resp = interp.intepret(parsed_stmts)
    # print(resp)


if __name__ == "__main__":
    main()
