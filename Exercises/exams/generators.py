def even(gen):
    while True:
        n = next(gen)
        if n % 2 == 0:
            yield n

def stopAt(gen, max):
    while True:
        n = next(gen)
        if n > max:
            return
        yield n

def buffer(gen, size):
    buf = []
    while True:
        try: n = next(gen)
        except StopIteration:
            if buf: yield buf
            return
        buf.append(n)
        if len(buf) == size:
            yield buf
            buf = []

def conditional(gen, pred):
    n = next(gen)
    while True:
        m = next(gen)
        if pred(m):
            yield n
        n = m

def fib():
    x,y = 1,1
    while True:
        yield x
        x,y = y, x+y

if __name__ == "__main__":
    even_fib = even(fib())
    for i in range(10): print(next(even_fib), end=' ')
    print()

    for i in stopAt(even(fib()), 40000000): print(i, end=' ')
    print()

    buffered_limited_fib = buffer(stopAt(fib(),3000), 5)
    for i in buffered_limited_fib: print(i)

    condfib = conditional(fib(), lambda x: (x%2 == 0))
    for i in range(10): print(next(condfib), end=' ')
    print()

    condfib2 = conditional(fib(), lambda x: (x%2 != 0))
    for i in range(15): print(next(condfib2), end=' ')
    print()
