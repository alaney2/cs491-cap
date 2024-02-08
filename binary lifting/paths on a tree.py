import math

class Tree:
    def __init__(self, n):
        self.n = n
        self.log = math.ceil(math.log2(n))
        self.ancestor = [[-1 for _ in range(self.log + 1)] for _ in range(n + 1)]
        self.depth = [0] * (n + 1)
        self.adj = [[] for _ in range(n + 1)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, node, parent):
        self.depth[node] = self.depth[parent] + 1
        self.ancestor[node][0] = parent
        for i in range(1, self.log + 1):
            self.ancestor[node][i] = self.ancestor[self.ancestor[node][i - 1]][i - 1]
        for child in self.adj[node]:
            if child != parent:
                self.dfs(child, node)

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        for i in range(self.log, -1, -1):
            if self.depth[u] - (1 << i) >= self.depth[v]:
                u = self.ancestor[u][i]
        if u == v:
            return u
        for i in range(self.log, -1, -1):
            if self.ancestor[u][i] != self.ancestor[v][i]:
                u = self.ancestor[u][i]
                v = self.ancestor[v][i]
        return self.ancestor[u][0]

    def distance(self, u, v):
        lca_node = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[lca_node]

    def add_leaf(self, parent, new_node):
      # Resize the structures if the new_node index is beyond the current size.
      while new_node >= len(self.adj):
          self.adj.append([])
          self.depth.append(0)
          self.ancestor.append([-1 for _ in range(self.log + 1)])

      # Add the new node as a leaf to its parent
      self.adj[parent].append(new_node)
      self.adj[new_node].append(parent)

      # Update depth for the new node
      self.depth[new_node] = self.depth[parent] + 1

      # Update the ancestor table for the new node
      self.ancestor[new_node][0] = parent
      for i in range(1, self.log + 1):
          if self.ancestor[new_node][i-1] != -1:
              self.ancestor[new_node][i] = self.ancestor[self.ancestor[new_node][i-1]][i-1]




n, m = map(int, input().split())
tree = Tree(n)

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree.add_edge(u, v)

tree.dfs(1, 0)

for _ in range(m):
    t, a, b = map(int, input().split())
    if t == 1:
        tree.add_leaf(a, b)
    elif t == 2:
        print(tree.distance(a, b))
