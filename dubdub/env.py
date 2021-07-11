from typing import Any, Dict, Optional

from pydantic import BaseModel

from dubdub import Token, dataclass


class Environment:
    values: Dict[str, Any] = {}
    enclosing: Optional["Environment"] = None

    def define(self, name: str, value):
        self.values[name] = value

    def access(self, name: Token):
        if name.lexeme in self.values:
            return self.values.get(name.lexeme)

        if self.enclosing is not None:
            return self.enclosing.access(name)

        raise RuntimeError(f"Undefined variable '{name.lexeme}'")

    def assign(self, name: Token, value: Any):
        if name.lexeme in self.values:
            self.values[name] = value
            return
        if self.enclosing is not None:
            return self.enclosing.assign(name, value)

        raise RuntimeError(f"Undefined variable '{name.lexeme}'")

    def ancestor(self, distance: int):
        environment: Environment = self
        for _ in range(distance):
            environment = environment.enclosing
        return environment

    def get_at(self, distance: int, name: str):
        self.ancestor(distance).values.get(name, None)

    def assign_at(self, distance: int, name: Token, value: Any):
        self.ancestor(distance).values[name.lexeme] = value
