
class calculator:
    def __init__(self, string):
        self.ex = calculator.parse(string)

    def __repr__(self):
        return repr(self.ex)

    def parse(string):
        from collections import deque
        stack = deque()
        for s in reversed(string):
            if s in "+-*/":
                assert len(stack) >= 2
                stack.append(expr(s, stack.pop(), stack.pop()))
            else:
                stack.append(int(s))
        assert len(stack) == 1
        return stack.pop()

class expr:
    def __init__(self, op, a, b):
        self.op = op
        self.a = a
        self.b = b

    def __repr__(self):
        return f"({self.a}{self.op}{self.b})"

    def is_calculable(self):
        return type(self.a) == type(self.b) == int

    def calculate(self):
        assert self.is_calculable()
        return ops[self.op](int(self.a), int(self.b))

    def propagate_calc(self):
        assert not self.is_calculable()
        for who in "ab":
            if type(self.__dict__[who]) == expr:
                if self.__dict__[who].is_calculable():
                    self.__dict__[who] = self.__dict__[who].calculate()
                else:
                    self.__dict__[who].propagate_calc()

ops = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}

def retprint(what):
    print(what)
    return what

def print_reduction(calc):
    while not calc.ex.is_calculable():
        print(calc)
        calc.ex.propagate_calc()
    else:
        print(calc)
        print(calc.ex.calculate())

if __name__ == "__main__":
    expressions = ["+34", "+3-15", "*+34-23", "+7++34+23", "*+*34-34/6-35", "/+-81*45*/93/52", "*+/12/14-2/32", "+2*-53/63"]
    [print_reduction(calculator(expr)) for expr in expressions]
