#include <iostream>
#include <vector>

using namespace std;

bool canDivide(const vector<vector<int>>& days, int n) {
    for (int i = 0; i < 5; ++i) {
        for (int j = i + 1; j < 5; ++j) {
            int count_i = 0, count_j = 0, count_both = 0;
            for (const auto& d : days) {
                bool avail_i = d[i], avail_j = d[j];
                if (avail_i && avail_j) count_both++;
                else if (avail_i) count_i++;
                else if (avail_j) count_j++;
            }

            if (count_i <= n / 2 && count_j <= n / 2 && count_i + count_j + count_both >= n) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> days(n, vector<int>(5));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < 5; ++j)
                cin >> days[i][j];

        cout << (canDivide(days, n) ? "YES" : "NO") << endl;
    }

    return 0;
}
