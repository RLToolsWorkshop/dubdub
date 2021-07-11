import time
from typing import Optional

from auto_all import end_all, start_all

import dubdub.interpreter as interp
from dubdub.dubcall import DubCallable
from dubdub.env import Environment
from dubdub.operations import *

start_all(globals())


class Clock(DubCallable):
    def arity(self) -> int:
        return 0

    def call(self, inter: "interp.Interpreter", args: List[Any]) -> float:
        return time.time() / 1000.0

    def __str__(self):
        return "<native fn>"


@dataclass
class Function(Stmt):
    name: Token
    body: List[Expr] = field(default_factory=[])
    params: List[Token] = field(default_factory=[])


@dataclass
class DubFunction(DubCallable):
    declaration: Function
    closure: Optional[Environment] = None

    def arity(self) -> int:
        return len(self.declaration.params)

    def call(self, interpreter: "interp.Interpreter", *args):
        environ = Environment(enclosing=self.closure)
        for arg, param in zip(args, self.declaration.params):
            environ.define(param.lexeme, arg)

        try:
            interpreter.execute_block(self.declaration.body, environ)
        except ReturnErr as ret:
            return ret.value

    def __str__(self):
        return f"<native {self.declaration.name.lexeme}>"


end_all(globals())
