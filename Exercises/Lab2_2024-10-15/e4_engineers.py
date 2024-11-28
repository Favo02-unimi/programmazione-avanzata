# very very very slow
# ram fills up before solution

from math import sqrt

def divisors(n):
  div = set()
  for i in range(1, int(sqrt(n) + 1)):
    if n % i == 0:
      div.add(i)
      div.add(n//i)
  div.add(n)
  return div

def is_practical(n):
  wall = 0
  for d in divisors(n):

    for i in range(max(0, wall-d-1), wall+1):
      if i+d <= wall:
        continue
      if i+d != wall+1:
        return False

      wall = wall+1

      if wall == n:
        return True

def primes():
  composite = {}
  cur = 2

  while True:
    if cur not in composite:
      yield cur
      composite[cur * cur] = [cur]
    else:
      for c in composite[cur]:
        composite.setdefault(c + cur, []).append(c)
      del composite[cur]

    cur += 1

# find triple primes pair
PRACTICAL = [-8, -4, 0, 4, +8]
sexy = []
last = None

res = []

for p in primes():
  if not last:
    last = p
    continue

  if p - last == 6:
    if sexy and sexy[-1][1] != last:
      sexy = []
    sexy.append((last, p))

  last = p

  if len(sexy) == 3:
    n = sexy[0][0] + (sexy[-1][1] - sexy[0][0]) // 2

    (a,b), (c,d), (e,f) = sexy
    assert a == n-9
    assert b == n-3
    assert c == n-3
    assert d == n+3
    assert e == n+3
    assert f == n+9

    for P in PRACTICAL:
      if not is_practical(n+P):
        print(f"invalid {n = } (found {len(res)})")
        break
    else:
      res.append(n)
      print(f"--- VALID {n = }")
      if len(res) == 4:
        break

    sexy = []

print(sum(res))
