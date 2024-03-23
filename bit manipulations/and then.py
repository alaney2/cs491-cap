tests = int(input())

for _ in range(tests):
  n = int(input())
  
  k = n
  while (k > 0):
    if k & (k - 1) == 0:
      print(k-1)
      break
    else:
      k = k & (k - 1)
