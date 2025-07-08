def logger(cls):
    class wrapped:
        def __init__(self, *args):
            self.instance = cls(*args)

        def __getattr__(self, name):
            if callable(self.instance.__class__.__dict__.get(name)):
                print("chiamato metodo", name)
            print("intercettazione", name)
            return getattr(self.instance, name)

        def __setattr__(self, name, value):
            print("intercettazione", name, value)
            if name == "instance":
                self.__dict__[name] = value
                return
            setattr(self.instance, name, value)

        def __str__(self):
            return str(self.instance)

    return wrapped

@logger
class test:
    def __init__(self, n, name, m):
        self.n = n
        self.m = m
        self.name = name

    def aaa(self):
        return 5

    def __str__(self):
        return f"{self.n} {self.name} {self.m}"

t = test(1, "ciao", 2)
print(t.n)
print(t.name)
print(t.m)
t.n = "ciao"
t.mmm = 89
print(t)
t.aaa()
