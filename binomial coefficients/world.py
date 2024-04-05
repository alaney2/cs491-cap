n, m, t = map(int, input().split())

from math import comb

count = 0
for boys in range(4, min(n+1, t)):
  girls = t - boys
  if girls > m or girls < 1:
    continue
  else:
    count += comb(n, boys) * comb(m, girls)
    
print(count)