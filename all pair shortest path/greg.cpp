#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;

int main() {
    int n;
    cin >> n;
    
    vvi graph(n + 1, vector<int>(n + 1));
    vi deletion_order(n + 1);
    vector<ll> shortest_path_sums(n + 1, 0);

    for (int vertex = 1; vertex <= n; ++vertex) {
        for (int j = 1; j <= n; ++j) {
            cin >> graph[vertex][j];
        }
    }

    for (int i = 1; i <= n; ++i) {
        cin >> deletion_order[i];
    }

    for (int k = n; k > 0; --k) {
        int kth = deletion_order[k];
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                int possible_shortest = graph[i][kth] + graph[kth][j];
                graph[i][j] = min(graph[i][j], possible_shortest);
            }
        }

        for (int i = k; i <= n; ++i) {
            for (int j = k; j <= n; ++j) {
                shortest_path_sums[k] += graph[deletion_order[i]][deletion_order[j]];
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << shortest_path_sums[i] << " ";
    }

    return 0;
}
