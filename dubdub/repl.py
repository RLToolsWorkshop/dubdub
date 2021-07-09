import abc
from ast import Dict
from datetime import datetime
from pathlib import Path
from typing import Any, List

from colorama import Fore, init
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
from dubdub.interpreter import Intepreter
from dubdub.parser import Parser
from dubdub.scanner import Scanner

init(autoreset=True)

success = lambda input: f"{Fore.GREEN}{input}"
failure = lambda input: f"{Fore.RED}{input}"


def scan_and_parse(line: str):
    scanner = Scanner(source=line)
    tokens: List[Token] = scanner.scan_tokens()

    parser = Parser(tokens=tokens)
    parsed = parser.parse()

    interp = Intepreter()
    response = interp.visit(parsed)

    print(tokens)
    print(parsed)
    print(response)


def run_repl() -> None:

    print("Welcome to dubdub-REPL")
    print("crtl-c to quit")
    try:
        while True:
            try:
                _in = input(">>> ")
                try:
                    print(scan_and_parse(_in))
                except:
                    out = scan_and_parse(_in)
                    if out != None:
                        print(out)
            except Exception as e:
                print(f"Error: {e}")
    except KeyboardInterrupt as e:
        print("\nExiting...")
