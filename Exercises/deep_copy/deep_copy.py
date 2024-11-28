import inspect
from copy import deepcopy

class Puffo():
  def __del__(self):
    print(f"DEL Puffo")

    frame = inspect.currentframe()
    back = frame.f_back

    print(f"current frame: line {frame.f_lineno}")
    print(f"current frame: line {back.f_lineno}")

    line = inspect.getframeinfo(back).code_context[0]
    fromm, to = map(str.strip, line.strip().split("="))
    back.f_globals[to] = deepcopy(back.f_globals[fromm])

print("-" * 20, "a = ...")

a = [1,2,3]

print("-" * 20, "b = ...")

# Senza questa riga inutile NON viene chiamato Puffo.__del__,
# quindi non avviene la deepcopy ma solo la shallow.
# Questo perchè `__del__` viene chiamato quando `b` viene sovrascritto, dovendo
# distruggere il valore assegnato precedentemente. Non ci interessa assolutamente
# di che tipo sia il nuovo tipo di `b`, `__del__` viene chiamato a prescindere.
b = Puffo()

print("-" * 20, "b = a")

b = a

print("-" * 20, "prints")

print(f"{a = }")
print(f"{b = }")

print("-" * 20, "b[0] = ...")

b[0] = "ciao"

print("-" * 20, "prints")

print(f"{a = }")
print(f"{b = }")

print("-" * 20, "fine")
