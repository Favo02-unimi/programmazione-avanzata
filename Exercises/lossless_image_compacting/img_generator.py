import sys
import random

IMG_SQUARE_SIDE = 2**12
IMG_SIZE = IMG_SQUARE_SIDE**2

print("img size: ", IMG_SIZE, file=sys.stderr)

for _ in range(IMG_SIZE):
  print(random.randint(0, 1), end=" ")
print()
