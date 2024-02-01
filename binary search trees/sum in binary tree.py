tests = int(input())

for _ in range(tests):
  vertex = int(input())
  s = vertex
  while vertex != 0:
    vertex //= 2
    s += vertex
  print(s)
  