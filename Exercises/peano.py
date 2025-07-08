import sys
sys.setrecursionlimit(10**5)

class NegativeNumber(Exception):
    pass

class DivisionByZero(Exception):
    pass

class InvalidPrev(Exception):
    pass

class zero:
    def __repr__(self):
        return "0"

class succ:
    def __init__(self, prev):
        match prev:
            case zero() | succ(): self.prev = prev
            case _: raise InvalidPrev("Invalid parameter to succ constructor")

    def __repr__(self):
        return f"succ({repr(self.prev)})"

def evaluate(peano):
    match peano:
        case zero(): return 0
        case _: return 1 + evaluate(peano.prev)

def convert(num, peano=zero()):
    match num == evaluate(peano):
        case True: return peano
        case _: return convert(num, succ(peano))

def add(a, b):
    match b:
        case zero(): return a
        case _: return add(succ(a), b.prev)

def sub(a, b):
    match a, b:
        case _, zero(): return a
        case zero(), _: raise NegativeNumber("Invalid subtraction")
        case _: return sub(a.prev, b.prev)

def mult(a, b):
    def _mult(a, b, res):
        match b:
            case zero(): return res
            case _: return _mult(a, b.prev, add(res, a))
    return _mult(a, b, zero())

def div(a, b):
    def _div(a, b, res):
        match b:
            case zero(): raise DivisionByZero("Invalid division")
            case _:
                try:
                    return _div(sub(a, b), b, succ(res))
                except NegativeNumber:
                    return res
    return _div(a, b, zero())

if __name__ == "__main__":

    try:
        succ(4)
    except InvalidPrev as e:
        print(e.args[0])

    first = zero()
    one = succ(first)
    second = succ(one)
    third = succ(succ(one))

    print(f"Zero: {first}\nOne: {one}\nSecond: {second}\nThird: {third}")

    print(f"Zero: {evaluate(first)}\nOne: {evaluate(one)}\nSecond: {evaluate(second)}\nThird: {evaluate(third)}")

    print(f"Zero: {convert(0)}\nOne: {convert(1)}\nSecond: {convert(2)}\nThird: {convert(3)}")


    print(f"7 + 15: {evaluate(add(convert(7), convert(15)))}")
    print(f"15 - 4: {evaluate(sub(convert(15), convert(4)))}")
    print(f"2 * 4: {evaluate(mult(convert(2), convert(4)))}")
    print(f"1000/2: {evaluate(div(convert(1000), convert(2)))}")
    print(f"15/7: {evaluate(div(convert(15), convert(7)))}")

    try:
        print(f"4 - 15: {evaluate(sub(convert(4), convert(15)))}")
    except NegativeNumber as e:
        print(e.args[0])

    try:
        print(f"15/0: {evaluate(div(convert(15), convert(0)))}")
    except DivisionByZero as e:
        print(e.args[0])
