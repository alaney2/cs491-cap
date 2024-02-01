#include <iostream>
#include <map>
#include <set>

int main() {
    std::set<int> sorted_set;
    std::map<int, std::pair<int, int>> children;

    int n;
    int a;
    std::cin >> n;
    std::cin >> a;
    sorted_set.insert(a);
    children[a] = {-1, -1};

    for (int i = 1; i < n; ++i) {
        std::cin >> a;
        auto it = sorted_set.upper_bound(a);

        if (it == sorted_set.end() || children[*it].first >= 0) {
            --it; 
            children[*it].second = a;
        } else {
            children[*it].first = a;
        }

        sorted_set.insert(a); 
        children[a] = {-1, -1};

        std::cout << *it << " ";
    }

    std::cout << std::endl;
    return 0;
}
