from nodes import ProgramNode, RuleNode, AndNode, CompareNode, FactNode, ActionNode


class State:
    def __init__(self):
        self.variables = {}
        self.hechos = set()
        self.hechos_iniciales = set()

    def __repr__(self):
        return f"State(variables={self.variables}, hechos={self.hechos})"


class Interpreter:
    def __init__(self, program: ProgramNode, state: State):
        self.program = program
        self.state = state

    def evaluar(self, nodo):
        if isinstance(nodo, CompareNode):
            if nodo.id not in self.state.variables:
                return False
            valor = self.state.variables[nodo.id]
            if nodo.op == ">": return valor > nodo.value
            if nodo.op == "<": return valor < nodo.value
            if nodo.op == "=": return valor == nodo.value

        if isinstance(nodo, FactNode):
            return nodo.id in self.state.hechos

        if isinstance(nodo, AndNode):
            return self.evaluar(nodo.left) and self.evaluar(nodo.right)

    def ejecutar(self):
        while True:
            nuevos = set()
            for regla in self.program.rules:
                if self.evaluar(regla.condition):
                    nuevos.add(regla.action.id)
            if nuevos.issubset(self.state.hechos):
                break
            self.state.hechos.update(nuevos)

    def output(self):
        hechos_activados = self.state.hechos - self.state.hechos_iniciales
        if not hechos_activados:
            print("(no output)")
        else:
            for hecho in sorted(hechos_activados):
                print(hecho)


def parse_state(text: str) -> State:
    state = State()
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        if "=" in line:
            partes = line.split("=")
            name = partes[0].strip()
            value = int(partes[1].strip())
            state.variables[name] = value
        else:
            state.hechos.add(line)
            state.hechos_iniciales.add(line)
    return state