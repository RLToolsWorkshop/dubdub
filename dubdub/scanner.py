from typing import List

from plum import dispatch

from dubdub import dataclass
from dubdub.primatives import Token
from dubdub.primatives.types import TokenTypes


@dataclass
class Scanner:
    source: str
    tokens: List[Token] = []
    
    # Scanner/Lexer Tracker
    start: int = 0
    current: int = 0
    line: int = 1
    
    def scan_tokens(self) -> List[Token]:
        return []
    
    def is_end(self) -> bool:
        return self.current >= len(self.source)
    
    def advance(self):
        self.current += 1
        return self.source[self.current]
    
    @dispatch
    def add_token(self, token_type: TokenTypes):
        pass
