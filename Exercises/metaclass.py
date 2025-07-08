def logger(f):
    def wrapped(*args):
        print(f"calling {f.__name__}{args}")
        return f(*args)
    return wrapped

class DecorateAll(type):
    def __new__(cls, name, super, cdict):
        print(f"new\n  {cls=}\n  {name=}\n  {super=}\n  {cdict=})\n")
        for k, v in cdict.items():
            if callable(v):
                cdict[k] = logger(v)
        return type.__new__(cls, name, super, cdict)

    def __init__(self, name, super, cdict):
        print(f"new\n  {self=}\n  {name=}\n  {super=}\n  {cdict=})\n")
        return type.__init__(self, name, super, cdict)

    def __call__(self, *args):
        print(f"call\n  {self=}\n  {args=}\n")
        return type.__call__(self, *args)

class Test(metaclass=DecorateAll):
    def prova(self):
        print("prova")

    def static():
        print("ciao")

t = Test()
t.prova()
Test.static()
