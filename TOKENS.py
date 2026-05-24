from dataclasses import dataclass
from enum import Enum
class Tokens_type(Enum):
       RULE_TK=1
       IF_TK=2
       THEN_TK=3
       LF_ARROW_TK=4
       RT_ARROW_TK=5
       AND_TK=6
       EQUAL_TK=7
       COLON_TK=8
       ID_TK=9
       NEWLINE_TK=10
       NUM_TK=11


@dataclass
class Tokens:
    def __init__(self,token_type: Tokens_type,lexeme:str,value:None):
           self.type = token_type
           self.lexeme = lexeme
           self.value = value

    def __repr__(self):
           return f"Token({self.type}, '{self.lexeme}', value={self.value})"