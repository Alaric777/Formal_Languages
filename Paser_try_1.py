from TOKENS import Tokens_type
from nodes import ProgramNode, RuleNode, AndNode, CompareNode, FactNode, ActionNode


class Parser_try:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        # Allow empty token list (program with no rules is valid)
        self.current_token = self.tokens[self.pos] if tokens else None

    def eat_tokens(self, token_type):
        if self.current_token and self.current_token.type == token_type:
            value = self.current_token
            self.pos += 1
            self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None
            return value
        else:
            found = self.current_token.type if self.current_token else "EOF"
            raise SyntaxError(f"Se esperaba {token_type}, se encontro {found}")

    def Program_Parsing(self):
        rules = self.RuleList_Parsing()
        return ProgramNode(rules)

    def RuleList_Parsing(self):
        rules = []
        # while instead of if: parse ALL rules, not just the first one
        while self.current_token and self.current_token.type == Tokens_type.RULE_TK:
            rules.append(self.Rule_Parsing())
        return rules

    def Rule_Parsing(self):
        self.eat_tokens(Tokens_type.RULE_TK)
        name = self.eat_tokens(Tokens_type.ID_TK).lexeme
        self.eat_tokens(Tokens_type.COLON_TK)
        self.eat_tokens(Tokens_type.IF_TK)
        condition = self.Cond_Paring()
        self.eat_tokens(Tokens_type.THEN_TK)
        action = self.Action_Parsing()
        return RuleNode(name, condition, action)

    def Cond_Paring(self):
        left = self.Atom_Parsing()
        return self.Cond_Dash_parsing(left)

    def Cond_Dash_parsing(self, left):
        if self.current_token and self.current_token.type == Tokens_type.AND_TK:
            self.eat_tokens(Tokens_type.AND_TK)
            right = self.Atom_Parsing()
            node = AndNode(left, right)
            return self.Cond_Dash_parsing(node)
        return left

    def Atom_Parsing(self):
        id_name = self.eat_tokens(Tokens_type.ID_TK).lexeme
        return self.Atom_Dash_parsing(id_name)

    def Atom_Dash_parsing(self, id_name):
        operation = (Tokens_type.RT_ARROW_TK, Tokens_type.LF_ARROW_TK, Tokens_type.EQUAL_TK)
        if self.current_token and self.current_token.type in operation:
            op = self.RelOp_Parsing()
            value = int(self.eat_tokens(Tokens_type.NUM_TK).lexeme)
            return CompareNode(id_name, op, value)
        return FactNode(id_name)

    def RelOp_Parsing(self):
        if self.current_token.type == Tokens_type.RT_ARROW_TK:
            self.eat_tokens(Tokens_type.RT_ARROW_TK)
            return ">"
        elif self.current_token.type == Tokens_type.LF_ARROW_TK:
            self.eat_tokens(Tokens_type.LF_ARROW_TK)
            return "<"
        elif self.current_token.type == Tokens_type.EQUAL_TK:
            self.eat_tokens(Tokens_type.EQUAL_TK)
            return "="
        raise SyntaxError("relational operator unrecognized")

    def Action_Parsing(self):
        return ActionNode(self.eat_tokens(Tokens_type.ID_TK).lexeme)