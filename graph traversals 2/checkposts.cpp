#include <iostream>
#include <vector>
#include <stack>
#include <climits>
using namespace std;

void dfs(int v, vector<bool>& visited, vector<vector<int>>& graph, vector<int>& result) {
    visited[v] = true;
    for (int i : graph[v]) {
        if (!visited[i]) {
            dfs(i, visited, graph, result);
        }
    }
    result.push_back(v);
}

vector<vector<int>> transpose(const vector<vector<int>>& graph, int n) {
    vector<vector<int>> g(n);
    for (int i = 0; i < n; ++i) {
        for (int j : graph[i]) {
            g[j].push_back(i);
        }
    }
    return g;
}

void fillOrder(vector<vector<int>>& graph, int n, vector<bool>& visited, stack<int>& stack) {
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            vector<int> temp;
            dfs(i, visited, graph, temp);
            for (int node : temp) {
                stack.push(node);
            }
        }
    }
}

vector<vector<int>> kosaraju(vector<vector<int>>& graph, int n) {
    stack<int> stack;
    vector<bool> visited(n, false);
    fillOrder(graph, n, visited, stack);

    vector<vector<int>> gr = transpose(graph, n);
    fill(visited.begin(), visited.end(), false);

    vector<vector<int>> sccs;
    while (!stack.empty()) {
        int i = stack.top();
        stack.pop();
        if (!visited[i]) {
            vector<int> scc;
            dfs(i, visited, gr, scc);
            sccs.push_back(scc);
        }
    }
    return sccs;
}

pair<long long, long long> solve(int n, vector<int>& costs, vector<vector<int>>& graph) {
    const int MOD = 1000000007;
    vector<vector<int>> sccs = kosaraju(graph, n);

    long long min_cost = 0, ways = 1;
    for (const auto& scc : sccs) {
        int min_scc_cost = INT_MAX;
        for (int i : scc) {
            min_scc_cost = min(min_scc_cost, costs[i]);
        }
        min_cost += min_scc_cost;

        int count = 0;
        for (int i : scc) {
            if (costs[i] == min_scc_cost) {
                count++;
            }
        }
        ways = (ways * count) % MOD;
    }
    return {min_cost, ways};
}

int main() {
    int n, m;
    cin >> n;
    vector<int> costs(n);
    for (int& cost : costs) {
        cin >> cost;
    }
    cin >> m;
    vector<vector<int>> graph(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        graph[u - 1].push_back(v - 1);
    }

    auto [min_cost, ways] = solve(n, costs, graph);
    cout << min_cost << " " << ways << endl;
    return 0;
}
