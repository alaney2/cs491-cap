def dfs_iterative(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)

n, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

count = 0
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs_iterative(graph, i, visited)

print(k - n + count)
