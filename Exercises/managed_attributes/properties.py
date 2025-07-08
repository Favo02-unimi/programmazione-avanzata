class account:
    def __init__(self, initial):
        self.bal = initial
    def withdraw(self, val):
        self.bal -= val
    def deposit(self, val):
        self.bal += val
    def balance(self):
        return self.bal

class safe_account(account):
    def __init__(self, initial):
        super().__init__(initial)
        self._amount = initial
    def safe_get(self):
        return self._amount
    def safe_set(self, val):
        assert val >= 0, "invalid bal"
        self._amount = val
    bal = property(safe_get, safe_set, None, "")

# aaa = safe_account(10)
# aaa.withdraw(5)
# print(aaa.balance())
# aaa.withdraw(5)
# print(aaa.balance())
# aaa.withdraw(5)
# print(aaa.balance())

class calc_account:
    def __init__(self, initial):
        self._add = initial
        self._sub = 0
    def withdraw(self, val):
        self._sub += val
    def deposit(self, val):
        self._add += val
    def calc(self):
        return self._add - self._sub
    def reset(self):
        self._add = 0
        self._sub = 0
    balance = property(calc, None, reset, "")

# bbb = calc_account(10)
# bbb.withdraw(5)
# print(bbb.balance)
# bbb.withdraw(5)
# print(bbb.balance)
# bbb.withdraw(5)
# print(bbb.balance)
# del bbb.balance
# print(bbb.balance)
