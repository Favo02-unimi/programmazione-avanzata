class safe_amount:
    def __get__(self, instance, owner):
        print(owner)
        return instance._amount
    def __set__(self, instance, amount):
        assert amount >= 0, "invalid amount"
        instance._amount = amount

class safe_account:
    def __init__(self, initial):
        self._amount = initial
    def withdraw(self, val):
        self.bal -= val
    def deposit(self, val):
        self.bal += val
    bal = safe_amount()

# sa = safe_account(5)
# print(sa.bal)
# sa.deposit(10)
# sa.withdraw(10)
# sa.withdraw(10)

class calc_amount:
    def __get__(self, instance, owner):
        return instance._add - instance._sub
    def __delete__(self, instance):
        instance._add = 0
        instance._sub = 0

class calc_account:
    def __init__(self, initial):
        self._add = initial
        self._sub = 0
    def withdraw(self, val):
        self._sub += val
    def deposit(self, val):
        self._add += val
    bal = calc_amount()

# ca = calc_account(10)
# print(ca.bal)
# ca.deposit(10)
# print(ca.bal)
# ca.withdraw(30)
# print(ca.bal)
# del ca.bal
# print(ca.bal)
