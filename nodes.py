class ProgramNode:

    def __init__(self, rules: list):
        # rules: List[RuleNode]
        self.rules = rules

    def __repr__(self):
        rules_str = "\n  ".join(repr(r) for r in self.rules)
        return f"ProgramNode(\n  {rules_str}\n)"


class RuleNode:

    def __init__(self, name: str, condition, action):
        self.name = name  # str
        self.condition = condition  # AndNode | CompareNode | FactNode
        self.action = action  # ActionNode

    def __repr__(self):
        return (
            f"RuleNode(name={self.name!r}, "
            f"condition={self.condition!r}, "
            f"action={self.action!r})"
        )


class AndNode:


    def __init__(self, left, right):
        self.left = left  # AndNode | CompareNode | FactNode
        self.right = right  # AndNode | CompareNode | FactNode

    def __repr__(self):
        return f"AndNode(left={self.left!r}, right={self.right!r})"


class CompareNode:

    def __init__(self, id: str, op: str, value: int):
        self.id = id  # str — identificador de la variable
        self.op = op  # str — '>', '<' o '='
        self.value = value  # int — literal entero

    def __repr__(self):
        return f"CompareNode({self.id!r} {self.op} {self.value})"


class FactNode:


    def __init__(self, id: str):
        self.id = id  # str

    def __repr__(self):
        return f"FactNode({self.id!r})"


class ActionNode:

    def __init__(self, id: str):
        self.id = id  # str

    def __repr__(self):
        return f"ActionNode({self.id!r})"
