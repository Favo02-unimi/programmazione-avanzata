# Indexing version: the original image is never copied.
# Faster than subslicing version (`subslicing.py`)

class QuadTree:

  def __init__(self, BITS, ORIGINAL_SIZE, size, row_offset=0, col_offset=0):
    same_color = True
    last = None

    for row in range(size):
      for col in range(size):
        index = (row + row_offset) * ORIGINAL_SIZE + (col + col_offset)
        if last is None:
          last = BITS[index]
        elif BITS[index] != last:
          same_color = False

    if same_color:
      self.color = "black" if last else "white"

    else:
      assert size > 1
      self.color = "gray"
      self.childs = []
      self.childs.append(QuadTree(BITS, ORIGINAL_SIZE, size//2, row_offset+0, col_offset+0))
      self.childs.append(QuadTree(BITS, ORIGINAL_SIZE, size//2, row_offset+0, col_offset+size//2))
      self.childs.append(QuadTree(BITS, ORIGINAL_SIZE, size//2, row_offset+size//2, col_offset+size//2))
      self.childs.append(QuadTree(BITS, ORIGINAL_SIZE, size//2, row_offset+size//2, col_offset+0))

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
qt = QuadTree(img, size, size)
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
