class Fact:
    def __init__(self, n):
        self.max = n
        self.num = 0
        self.res = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num == self.max:
            raise StopIteration
        res = self.res
        self.num += 1
        self.res *= self.num
        return res

f = Fact(10)
it = iter(f)
print(list(it))
