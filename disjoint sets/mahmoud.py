from collections import deque

n = int(input())
edges = []
for _ in range(n-1):
  start, end = map(int, input().split())
  edges.append((start, end))
  

graph = [[] for _ in range(n)]
for u, v in edges:
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

colors = [-1] * n

# BFS
queue = deque([0])
colors[0] = 0
red_count, blue_count = 1, 0

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if colors[neighbor] == -1:
            colors[neighbor] = 1 - colors[node]
            queue.append(neighbor)
            if colors[neighbor] == 0:
                red_count += 1
            else:
                blue_count += 1

max_edges = red_count * blue_count - (n - 1)

print(max_edges)