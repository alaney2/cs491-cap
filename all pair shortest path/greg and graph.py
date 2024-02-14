n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
deletion_order = [0] * (n + 1)
shortest_path_sums = [0] * (n + 1)

for vertex in range(1, n + 1):
    graph[vertex][1:] = map(int, input().split())

deletion_order[1:] = map(int, input().split())

for k in range(n, 0, -1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            possible_shortest = graph[i][deletion_order[k]] + graph[deletion_order[k]][j]
            graph[i][j] = min(graph[i][j], possible_shortest)

    for i in range(k, n + 1):
        for j in range(k, n + 1):
            shortest_path_sums[k] += graph[deletion_order[i]][deletion_order[j]]

for sum in shortest_path_sums[1:]:
    print(sum, end=" ")
