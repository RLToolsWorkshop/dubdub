import abc
from typing import Any

from dubdub import dataclass
from dubdub import interpreter as itr


@dataclass
class DubCallable(abc.ABC):
    @abc.abstractmethod
    def arity(self) -> int:
        pass

    @abc.abstractmethod
    def call(self, inter: "Any", *args):
        pass
