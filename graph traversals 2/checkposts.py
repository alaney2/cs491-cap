def dfs(graph, v, visited, stack):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, stack)
    stack = stack.append(v)

def transpose(graph, n):
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            g[j].append(i)
    return g

def fillOrder(graph, n, visited, stack):
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, stack)

def kosaraju(graph, n):
    stack = []
    visited = [False] * n

    fillOrder(graph, n, visited, stack)

    gr = transpose(graph, n)

    visited = [False] * n

    scc_costs = []
    while stack:
        i = stack.pop()
        if not visited[i]:
            scc = []
            dfs(gr, i, visited, scc)
            scc_costs.append(scc)

    return scc_costs

def solve(n, costs, graph):
    MOD = 1000000007

    sccs = kosaraju(graph, n)
    min_cost = 0
    ways = 1

    for scc in sccs:
        min_scc_cost = min(costs[i] for i in scc)
        min_cost += min_scc_cost
        ways = (ways * sum(costs[i] == min_scc_cost for i in scc)) % MOD

    return min_cost, ways

# Example usage
n = 5  # Number of junctions
costs = [1, 2, 3, 4, 5]  # Costs for each junction
m = 4  # Number of roads
edges = [(0, 1), (1, 2), (2, 0), (3, 4)]  # Edges representing one-way roads

graph = [[] for _ in range(n)]
for u, v in edges:
    graph[u].append(v)

print(solve(n, costs, graph))
