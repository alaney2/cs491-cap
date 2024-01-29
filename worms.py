n = int(input())

pile = [int(x) for x in input().split()]

for i in range(1, n):
  pile[i] += pile[i-1]
min_ = pile[0]
max_ = pile[-1]

num_worms = int(input())
worms = [int(x) for x in input().split()]

for i in range(num_worms):
  x = worms[i]
  if x > max_:
    print(n)
    continue
  if x < min_:
    print(1)
    continue
  lower = 0
  upper = n-1
  while lower < upper:
    mid = (lower + upper) // 2
    if pile[mid] < x:
      lower = mid + 1
    else:
      upper = mid
  print(lower+1)
    