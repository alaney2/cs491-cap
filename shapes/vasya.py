n, d = map(int, input().split())
m = int(input())
for _ in range(m):
  x, y = map(int, input().split())
  if (x - d <= y <= x + d) and (-x + d <= y <= -x + 2 * n - d):
    print('YES')
  else:
    print('NO')