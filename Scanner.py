from TOKENS import Tokens,Tokens_type

class Lexer:

        def __init__(self,text)->None:
            self.it = iter(text)
            self.current=None

        def advance(self):
            try:
                self.current=next(self.it)

            except StopIteration:
                self.current=None

        def Lexer_god(self):

            while self.current is not None:

                if self.current.isalpha():
                  lexeme = ""
                  while self.current is not None and (
                    self.current.isalpha() or self.current.isdigit() or self.current == "_"):
                    lexeme += self.current
                    self.advance()
                  keywords = {
                    "rule": Tokens_type.RULE_TK,
                    "if": Tokens_type.IF_TK,
                    "then": Tokens_type.THEN_TK,
                    "AND": Tokens_type.AND_TK,
                  }
                  if lexeme in keywords:
                    return Tokens(keywords[lexeme], lexeme, None)
                  else:
                    return Tokens(Tokens_type.ID_TK, lexeme, None)

                elif self.current == "\n":
                    self.advance()
                    return Tokens(Tokens_type.NEWLINE_TK,"\n",None)


                elif self.current in ("\t"," "):
                    self.advance()
                    continue

                elif self.current==">":
                    self.advance()
                    return Tokens(Tokens_type.RT_ARROW_TK,">",None)

                elif self.current=="<":
                    self.advance()
                    return Tokens(Tokens_type.LF_ARROW_TK,"<",None)

                elif self.current==":":
                    self.advance()
                    return Tokens(Tokens_type.COLON_TK,":",None)

                elif self.current=="=":
                    self.advance()
                    return Tokens(Tokens_type.EQUAL_TK,"=",None)

                elif self.current.isdigit():
                    lexeme = ""
                    while self.current is not None and self.current.isdigit():
                       lexeme += self.current
                       self.advance()
                    return Tokens(Tokens_type.NUM_TK, lexeme, int(lexeme))

                else:
                    raise Exception(f"Unrecognized character {self.current}")
            return None

        def LexearAll(self):
            tokens_def=[]
            self.advance()
            while True:
                token=self.Lexer_god()
                if token is None:
                    break
                tokens_def.append(token)
            return tokens_def
