import abc
from ast import Dict
from datetime import datetime
from pathlib import Path
from typing import Any, List

from dubdub import Binary, Grouping, Literal, Token, Unary, Visitor, dataclass

CWD_DIR = Path.cwd()


@dataclass
class Intepreter(Visitor):
    pass
