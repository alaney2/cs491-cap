n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    source, dest = map(int, input().split())
    graph[source - 1].append(dest)
    graph[dest - 1].append(source)

connection_counts = [len(connections) for connections in graph]

if connection_counts.count(1) == 2 and connection_counts.count(2) == n - 2:
    print('bus topology')
elif all(len(connections) == 2 for connections in graph):
    print('ring topology')
elif connection_counts.count(1) == n - 1 and connection_counts.count(n - 1) == 1:
    print('star topology')
else:
    print('unknown topology')
