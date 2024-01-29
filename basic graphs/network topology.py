import sys

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
  
for i in range(m):
  source, dest = map(int, input().split())

  graph[source-1].append(dest)
  # graph[dest-1].append(source)
  
# print(graph)

is_bus = True
check_bus = [False for _ in range(n)]
for i in range(n):
  if len(graph[i]) > 1:
    is_bus = False
    break
  if len(graph[i]) == 1:
    check_bus[graph[i][0] - 1] = not check_bus[graph[i][0] - 1]

if is_bus:
  if check_bus.count(False) == 1:
    print('bus topology')
    sys.exit(0)
  elif check_bus.count(False) == 0:
    print('ring topology')
    sys.exit(0)

is_star = True
check_star = [-1 for _ in range(n)]
for i in range(n):
  if len(graph[i]) > 0:
    if len(graph[i]) == n - 1:
      check_star[i] = 1
    else:
      is_star = False
      break
  if len(graph[i]) == 0:
    check_star[i] = 0

if not is_star:
  print('unknown topology')
  sys.exit(0)

if check_star.count(1) == 1 and check_star.count(0) == n - 1:
  print('star topology')
  sys.exit(0)
  
  
print('unknown topology')
