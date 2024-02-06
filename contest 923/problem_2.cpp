#include <iostream>
#include <vector>
#include <string>

int main() {
    int t;
    std::cin >> t;

    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;

        std::vector<int> arr(n);
        for (int j = 0; j < n; ++j) {
            std::cin >> arr[j];
        }

        std::string result;
        std::vector<int> letters(n, 0);

        for (int num : arr) {
            result += char('a' + letters[num]);
            letters[num]++;
        }

        std::cout << result << std::endl;
    }

    return 0;
}
