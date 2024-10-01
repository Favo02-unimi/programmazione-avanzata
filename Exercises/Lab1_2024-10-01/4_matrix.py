def pprint(matrix):
  for row in matrix:
    print(row)

def identity(n):
  return [[1 if row == col else 0 for col in range(n)] for row in range(n)]

def square(n):
  return [[1 + col + row*n for col in range(n)] for row in range(n)]

def traspose(matrix):
  return [[row[col] for row in matrix] for col in range(len(matrix[0]))]

def multiply(m1, m2):
  assert len(m1[0]) == len(m2)
  getcol = lambda matrix, i: [row[i] for row in matrix]
  return [[sum(a*b for a,b in zip(row, getcol(m2, col))) for col in range(len(m2[0]))] for row in m1]

n = int(input("Matrix size: "))
pprint(identity(n))
print()
pprint(square(n))
print()
pprint(traspose(square(n)))
print()
pprint(traspose([[1],[2],[3],[4]]))
print()
pprint(traspose([[1,2,3, 4]]))
print()
pprint(multiply([[1,2,3],[4,5,6]], [[7,8],[9,10],[11,12]]))
