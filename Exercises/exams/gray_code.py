def memoization(f):
    mem = {}
    def wrapped(*args):
        if args in mem:
            print(f"\n### cached value for {args} --> {mem[args]}")
            return mem[args]
        res = list(f(*args))
        mem[args] = res
        return res
    return wrapped

def gray(n):
    if n == 1:
        yield "0"
        yield "1"
        return
    prev = list(gray(n-1))
    for p in prev:
        yield "0" + p
    for p in reversed(prev):
        yield "1" + p

@memoization
def mgray(n):
    if n == 1:
        yield "0"
        yield "1"
        return
    prev = list(mgray(n-1))
    for p in prev:
        yield "0" + p
    for p in reversed(prev):
        yield "1" + p

if __name__ == "__main__":
    print( "GC(1) :-", end=" ")
    for gc in gray(1): print(gc, end=" ")
    print( "\nGC(2) :-", end=" ")
    for gc in gray(2): print(gc, end=" ")
    print( "\nGC(3) :-", end=" ")
    for gc in gray(3): print(gc, end=" ")
    print( "\nGC(4) :-", end=" ")
    for gc in gray(4): print(gc, end=" ")
    print()
    print( "GC_(1) :-", end=" ")
    for gc in mgray(1): print(gc, end=" ")
    print( "\nGC_(2) :-", end=" ")
    for gc in mgray(2): print(gc, end=" ")
    print( "\nGC_(3) :-", end=" ")
    for gc in mgray(3): print(gc, end=" ")
    print( "\nGC_(4) :-", end=" ")
    for gc in mgray(4): print(gc, end=" ")
    print()
