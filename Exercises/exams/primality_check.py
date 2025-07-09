from math import sqrt, log2
from functools import cache
from random import randint

def trialdivision(p):
    for i in range(2, int(sqrt(p))+1):
        if p % i == 0: return False
    return True

def lucaslehmer(mp):

    @cache
    def _s(i):
        if i == 0: return 4
        return _s(i-1)**2 - 2

    p = log2(mp+1)
    if p - int(p) != 0: return False
    if not trialdivision(p): return False
    return _s(p-2) % mp == 0

def littlefermat(p):
    for a in (randint(1, p-1) for _ in range(int(log2(p)))):
        if pow(a, p-1, p) != 1: return False
    return True

trialdivision.name = "Trial-Division"
lucaslehmer.name = "Lucas-Lehmer"
littlefermat.name = "Little Fermat"

def is_prime(p):
    f = None
    if p <= 10_000: f = trialdivision
    elif p <= 524280: f = lucaslehmer
    else: f = littlefermat
    print(f"Calling {f.name}", end="\t")
    return f(p)

if __name__ == "__main__":
    primes = [25, 127, 8191, 131071, 524286, 524287, 524288, 2147483647]
    for p in primes:
        print(f"\t {p:14d} : {is_prime(p)}")
