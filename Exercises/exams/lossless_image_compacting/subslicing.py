# Subslicing version.
# Slower than subslicing version (`subslicing.py`)

class QuadTree:

  def __init__(self, bits):

    if all(bm == bits[0] for bm in bits):
      self.color = "black" if bits[0] else "white"

    else:
      self.color = "gray"

      cur_size = int(len(bits)**(1/2))
      new_size = cur_size // 2

      q12 = bits[:len(bits)//2]
      q34 = bits[len(bits)//2:]

      q1 = [q for i, q in enumerate(q12) if i % cur_size < new_size]
      q2 = [q for i, q in enumerate(q12) if i % cur_size >= new_size]
      q3 = [q for i, q in enumerate(q34) if i % cur_size < new_size]
      q4 = [q for i, q in enumerate(q34) if i % cur_size >= new_size]

      self.childs = [QuadTree(q1), QuadTree(q2), QuadTree(q4), QuadTree(q3)]

  def __repr__(self) -> str:
    return self.color

# 2x2
# img = [1,1,0,1]
# 4x4
# img = [0]*2 + [1]*2 + [0]*2 + [1]*2 + [0]*2 + [1]*2 + [0]*2 + [1]*2
# 16x16
# img = [0]*20 + [1]*3 + [0]*5 + [1]*2 + [0]*2 + [1]*6 + [0]*2 + [1]*6 + [0]*2 + [1]*4 + [0]*4 + [1]*4 + [0]*3 + [1]*1

# read image from input (`img_generator.py`)
img = list(map(int, input().split()))

size = int(len(img)**(1/2))

import timeit
start_time = timeit.default_timer()
qt = QuadTree(img)
end_time = timeit.default_timer()

def pprint(bits, size):
  for i in range(size):
    print(bits[i*size:(i+1)*size])

def dfs(start, depth=0) -> int:
  print(" " * depth, start.color, sep="")
  res = 1
  if start.color == "gray":
    for c in start.childs:
      res += dfs(c, depth+4)
  return res

print("\noriginal image:")
pprint(img, size)

print("\ncompressed image:")
nodes = dfs(qt)

print(f"\nQuadTree creation time: {end_time - start_time} seconds")
print(f"original image size: {len(img)}")
print(f"compressed image size: {nodes}")
