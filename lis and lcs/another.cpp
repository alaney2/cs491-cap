#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int lcs(const vector<int>& arr1, const vector<int>& arr2) {
    int n = arr1.size();
    int m = arr2.size();

    vector<int> prev(n + 1, 0);
    vector<int> curr(n + 1, 0);

    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (arr2[i - 1] == arr1[j - 1]) {
                curr[j] = prev[j - 1] + 1;
            } else {
                curr[j] = max(prev[j], curr[j - 1]);
            }
        }
        prev.swap(curr);
    }
    return prev[n];
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> arr1(n), arr2(n);
        for (int i = 0; i < n; ++i) {
            cin >> arr1[i];
        }
        for (int i = 0; i < n; ++i) {
            cin >> arr2[i];
        }
        int lcs_length = lcs(arr1, arr2);
        int min_removals = 2 * (n - lcs_length);
        cout << min_removals << endl;
    }
    return 0;
}
