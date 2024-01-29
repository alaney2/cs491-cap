#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool isSafe(const vector<int>& v, int row, int col) {
    for (int i = 0; i < row; ++i) {
				if (v[i] == -1) {
					continue;
				}
        if (v[i] == col || abs(row - i) == abs(col - v[i])) {
            return false;
        }
    }
    return true;
}

int countQueens(const vector<int>& v) {
    int queens = 0;
    for (int q : v) {
        if (q != -1) {
            queens++;
        }
    }
    return queens;
}

void with_separator(const vector<int>& vec,
                    string sep = " ")
{
    for (auto elem : vec) {
        cout << elem << sep;
    }
 
    cout << endl;
}

void placeQueens(int k, int n, int m, int row, vector<int>& v, int& solutions) {
    if (countQueens(v) == k) {
        solutions++;
				// with_separator(v);
        return;
    }

    if (row >= n) return;
		
    for (int col = 0; col < m; ++col) {
        if (isSafe(v, row, col)) {
            v[row] = col;
            placeQueens(k, n, m, row + 1, v, solutions);
            v[row] = -1;
        }
    }

    if (countQueens(v) < k) {
        placeQueens(k, n, m, row + 1, v, solutions);
    }
}

int main() {
    int k, n, m;
    cin >> k >> n >> m;
		if (n >= m) {
			int temp = n;
			n = m;
			m = temp;
		}
    if (k > n || k > m) {
				cout << 0 << endl;
        return 0;
    }

    int solutions = 0;
    vector<int> v(n, -1);

    placeQueens(k, n, m, 0, v, solutions);

    cout << solutions << endl;

    return 0;
}
