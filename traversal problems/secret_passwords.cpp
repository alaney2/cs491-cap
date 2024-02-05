#include <iostream>
#include <vector>

using namespace std;

int main() {
    const int N = 26;
    int n;
    cin >> n;

    vector<int> parent(N);
    vector<bool> char_in_password(N, false);

    for (int i = 0; i < N; ++i) {
        parent[i] = i;
    }

    for (int _ = 0; _ < n; ++_) {
        string password;
        cin >> password;
        vector<bool> current_password_chars(N, false);

        for (char &ch : password) {
            int index = ch - 'a';
            char_in_password[index] = current_password_chars[index] = true;
        }

        int first_connected_char = -1;
        for (int i = 0; i < N; ++i) {
            if (current_password_chars[i]) {
                first_connected_char = parent[i];
                break;
            }
        }

        // Union
        for (int i = 0; i < N; ++i) {
            if (current_password_chars[i]) {
                parent[parent[i]] = first_connected_char;
                parent[i] = first_connected_char;
            }
        }
    }

    int distinct_classes_count = 0;
    for (int i = 0; i < N; ++i) {
        if (char_in_password[i] && parent[i] == i) {
            ++distinct_classes_count;
        }
    }

    cout << distinct_classes_count << endl;

    return 0;
}
