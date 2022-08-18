import math
import random


class Equation:
    equation = ""
    solution = 0

    def __init__(self, equation):
        self.equation = equation
        if equation != "":
            self.solution = round(float(eval(equation)), 4)


class EquationCreator:
    equation = Equation("")
    num_range = (0, 100)
    num_steps = 0.1

    def __init__(self, num_range: tuple = (0, 100), num_steps: float = 0.1):
        self.num_range = num_range
        self.num_steps = num_steps

    def run(self):
        return self.equation


class EasyEquationCreator(EquationCreator):
    equation = Equation("")

    def __init__(self, num_range: tuple = (0, 100), num_steps: float = 1, operators: list = None):
        super().__init__(num_range, num_steps)
        self.operators = operators

    def run(self):
        if self.operators is None:
            self.operators = ["+", "-", "*", "/"]

        equation = ""
        l = math.log2(self.num_steps)

        while equation == "":
            n1 = round(
                random.randrange(int(self.num_range[0] / self.num_steps), int(self.num_range[1] / self.num_steps),
                                 step=1) * self.num_steps, int(l * -1))
            n2 = round(
                random.randrange(int(self.num_range[0] / self.num_steps), int(self.num_range[1] / self.num_steps),
                                 step=1) * self.num_steps, int(l * -1))
            operator = random.choice(self.operators)
            if operator == "/" and (
                    n2 == 0 or n1 == 0 or n1 < n2 or n1 % n2 != 0 or n1 == n2 or n1 == 1 or n2 == 1):
                continue
            elif operator == "*" and (n1 == 0 or n2 == 0 or n1 == 1 or n2 == 1):
                continue
            elif operator == "-" and (n1 == 0 or n2 == 0 or n1 == n2):
                continue

            equation = f"{n1} {operator} {n2}"

        self.equation = Equation(equation)
        return Equation(equation)


class SimpleEquationCreator(EquationCreator):
    equation = Equation("")

    def __init__(self, num_count: int = 2, num_range: tuple = (0, 100), num_steps: float = 0.1, operators=None):
        super().__init__(num_range, num_steps)
        self.num_count = num_count
        self.operators = operators

    def run(self):
        if self.operators is None:
            self.operators = ["+", "-", "*", "/"]

        equation = ""

        for i in range(self.num_count):
            n = random.randrange(int(self.num_range[0] / self.num_steps), int(self.num_range[1] / self.num_steps),
                                 step=1) * self.num_steps
            equation += str(n)
            equation += str(random.choice(self.operators))

        equation = equation[:-1]
        self.equation = Equation(equation)
        return Equation(equation)
