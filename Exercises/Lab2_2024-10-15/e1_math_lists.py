from functools import lru_cache
from math import lcm, factorial

# 1. Sum all the natural numbers below one thousand that are multiples of 3 or 5
one = sum(n for n in range(1000) if n % 3 == 0 or n % 5 == 0)
print("1: ", one)

# 2. Calculate the smallest number divisible by each of the numbers 1 to 20.
two = next(i for i in range(20, factorial(20), 20) if all(i % div == 0 for div in range(1, 21)))
assert two == lcm(*range(1, 20))
print("2: ", two)

# 3. Calculate the sum of the figures of 2^1000
three = sum(int(s) for s in str(2**1000))
print("3: ", three)

# 4. Calculate the first term in the Fibonacci sequence to contain 1000 digits.
@lru_cache(None)
def fib(n): return (n <= 2 and 1) or (fib(n-1) + fib(n-2))
four = next(fib(n) for n in range(10**1000) if len(str(fib(n))) >= 1000)
print("4: ", four)


