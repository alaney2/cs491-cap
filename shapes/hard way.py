
t = int(input())

for _ in range(t):
  x1, y1, = map(int, input().split())
  x2, y2 = map(int, input().split())
  x3, y3 = map(int, input().split())
  
  if y1 == y2 and y3 < y1:
    print(abs(x1 - x2))
  elif y1 == y3 and y2 < y1:
    print(abs(x1 - x3))
  elif y2 == y3 and y1 < y2:
    print(abs(x2 - x3))
  else:
    print(0)