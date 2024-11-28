from math import factorial as f

def sin(x, n=1000):
  return sum((-1 if (i+1) % 4 == 0 else 1) * (x**i / f(i)) for i in range(1, 2*n, 2))

def compare(x, maxprec=1000):
  from math import sin as mathsin
  for prec in range(maxprec):
    print(f"approx (prec {prec}): {sin(x, prec)} - real: {mathsin(x)} - diff: {abs(sin(x, prec) - mathsin(x))}")
