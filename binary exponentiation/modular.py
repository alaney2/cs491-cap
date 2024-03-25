t, m = map(int, input().split())

for _ in range(t):
  a, b = map(int, input().split())
  print(pow(a, b, m))