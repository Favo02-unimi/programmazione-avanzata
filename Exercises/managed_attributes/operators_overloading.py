class account:
    def __init__(self, initial):
        self.bal = initial
        self.name = "ciao"
    def withdraw(self, val):
        self.bal -= val
    def deposit(self, val):
        self.bal += val
    def balance(self):
        return self.bal

    def __getattr__(self, attr):
        print(f"invalid attr {attr}")

    def __getattribute__(self, attr):
        if attr == "bal":
            return self.__dict__["bal"]
        return super().__getattribute__(attr)

    def __setattr__(self, attr, value):
        if attr == "bal":
            assert value > 0, f"invalid balance {value}"
            self.__dict__["bal"] = value
            return
        super().__setattr__(attr, value)

    def __delattr__(self, attr):
        if attr == "bal":
            self.__dict__["bal"] = 0
            return
        super().__delattr__(attr)

a = account(10)
a.ajushdsa
print(a.balance())
del a.bal
print(a.bal)
a.withdraw(20)
