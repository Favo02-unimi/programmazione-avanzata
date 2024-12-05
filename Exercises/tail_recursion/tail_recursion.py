import sys

class TailRecException(Exception):
  def __init__(self, args, kwargs):
    self.args = args
    self.kwargs = kwargs

def tail_recursion(func):

  def wrapper(*args, **kwargs):

    f = sys._getframe()
    if f.f_back and f.f_back.f_back and \
       f.f_code == f.f_back.f_back.f_code:
      raise TailRecException(args, kwargs)

    while True:
      try:
        return func(*args, **kwargs)

      except TailRecException as e:
        args, kwargs = e.args, e.kwargs

  return wrapper

@tail_recursion
def fact(n, acc=1):
  if n == 0: return acc
  return fact(n-1, n*acc)

@tail_recursion
def fibo(n, a=2, b=1):
  if n <= 1: return b
  return fibo(n-1, a+b, a)

sys.setrecursionlimit(10)

print(fibo(1000))
print(fact(1000))
