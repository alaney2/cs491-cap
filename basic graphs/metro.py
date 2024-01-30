n, s = map(int, input().split())

forward = list(map(int, input().split()))
backward = list(map(int, input().split()))

start = 1

if forward[start-1] == 0:
    print("NO")
    exit(0)
    
for i in range(1, n):
  if forward[i] == 0 or i < s - 1:
    continue
  if forward[i] == 1:
    if i == s - 1:
      print('YES')
      exit(0)
    elif backward[i] == 1:
      # for j in range(i, s-2, -1):
      if backward[s-1] == 1:
        print('YES')
        exit(0)
        
print('NO')