# from Celsius to XX
toC = lambda c: c
toK = lambda c: c + 273.15
toF = lambda c: c * (9 / 5) + 32
toR = lambda c: (c + 273.15) * (9/5)
toD = lambda c: (100 - c) * (3/2)
toN = lambda c: c * (33/100)
toRe = lambda c: c * (4/5)
toRo = lambda c: c * (21/40) + 7.5

# from XX to Celsius
fromC = lambda c: c
fromK = lambda c: c - 273.15
fromF = lambda c: (c - 32) * (5 / 9)
fromR = lambda c: (c - 491.67) * (5/9)
fromD = lambda c: 100 - c * (2/3)
fromN = lambda c: c * (100/33)
fromRe = lambda c: c * (5/4)
fromRo = lambda c: (c - 7.5) * (40/21)

scales = {
  "C": (toC, fromC),
  "K": (toK, fromK),
  "F": (toF, fromF),
  "R": (toR, fromR),
  "D": (toD, fromD),
  "N": (toN, fromN),
  "Re": (toRe, fromRe),
  "Ro": (toRo, fromRo)
}

def table(pure):
  print(end="\t")
  for h in scales:
    print(h, end="\t")
  print()

  for scale_from, (_, fromm) in scales.items():
    print(scale_from, end="\t")
    c = fromm(pure)
    for (to, _) in scales.values():
      print(f"{to(c):.1f}", end="\t")
    print()

def toAll(temp, scale):
  c = scales[scale][1](temp)
  res = []
  for to in scales:
    res.append((scales[to][0](c), to))
  return list(map(lambda x: f"{x[0]:.1f} {x[1]}", sorted(res)))

pure = float(input("Pure number for table: "))
table(pure)

scale = input(f"Scale ({" ".join(list(scales.keys()))}):")
if scale not in scales.keys():
  raise ValueError("Invalid scale")
temp = float(input("Temperature to convert: "))
print(toAll(temp, "K"))
