
r, d = map(int, input().split())
t = int(input())
count = 0
for _ in range(t):
  xi, yi, ri = map(int, input().split())
  distance = (xi ** 2 + yi ** 2) ** 0.5
  if distance - ri >= r - d and distance + ri <= r:
    count += 1
print(count)