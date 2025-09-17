from collections import deque

class calculator:

    ops = {
        '+': (lambda a, b: a + b, 'add'),
        '-': (lambda a, b: a - b, 'sub'),
        '*': (lambda a, b: a * b, 'mul'),
        '/': (lambda a, b: a // b, 'div'),
    }

    def __init__(self, expr):

        def build():
            e = stack.popleft()
            if e in '+-*/':
                return expression(e, build(), build())
            return leaf(int(e))

        stack = deque(expr)
        self.expr = build()

    def eval(self):
        return self.expr.eval()

    def code(self):
        return "\n".join(self.expr.code())

class expression:
    def __init__(self, op, a, b):
        self.op = op
        self.a = a
        self.b = b
    def eval(self):
        return calculator.ops[self.op][0](self.a.eval(), self.b.eval())
    def code(self):
        return self.a.code() + self.b.code() + [ calculator.ops[self.op][1] ]
    def __str__(self):
        return f"({str(self.a)} {self.op} {str(self.b)})"

class leaf:
    def __init__(self, a):
        self.a = a
    def eval(self):
        return self.a
    def code(self):
        return [ f"store {self.a}" ]
    def __str__(self):
        return str(self.a)

if __name__ == "__main__":
    # calc = calculator('*+345')
    # calc = calculator('+2*-53/63')
    calc = calculator('-*54*23')
    print(calc.eval())
    print(calc.code())
