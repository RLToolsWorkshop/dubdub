from typing import Any, AnyStr

from dubdub import dataclass
from dubdub.primatives.types import TokenTypes


@dataclass
class Token:
    token_type: TokenTypes
    lexeme: str
    literal: AnyStr
    line: int
    
    def __str__(self) -> str:
        return f"Token(type={self.token_type}, lexeme={self.lexeme}, literal={self.literal})"

def main():
    sample = Token(token_type=TokenTypes.AND, lexeme="and", literal="and", line=1)
    print(sample)

if __name__ == "__main__":
    main()
