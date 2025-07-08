def memoization(f):
    mem = {}
    def wrapped(*args):
        if args in mem:
            return mem[args]
        res = f(*args)
        mem[args] = res
        return res
    return wrapped

class memoization:
    def __init__(self, f):
        self.f = f
        self._mem = {}
    def __call__(self, *args):
        if args in self._mem:
            return self._mem[args]
        res = self.f(*args)
        self._mem[args] = res
        return res

@memoization
def fibo(n):
    if n <= 2:
        return 1
    return fibo(n-2) + fibo(n-1)

print(fibo(37))
