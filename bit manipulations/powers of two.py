n, k = map(int, input().split())

min_ = 0
max_ = n

temp = n
while temp > 0:
  temp = temp & (temp - 1)
  min_ += 1

import heapq

if min_ <= k <= max_:
  print('YES')
  powers = []
  while n > 0 and len(powers) < k:
      power = 1
      while power * 2 <= n:
          power *= 2
      powers.append(power)
      n -= power
  powers = [-power for power in powers]
  heapq.heapify(powers)
  while len(powers) < k:
      power = heapq.heappop(powers)
      heapq.heappush(powers, power // 2)
      heapq.heappush(powers, power // 2)
      
  powers = [-power for power in powers]
  print(*powers)
else:
  print('NO')