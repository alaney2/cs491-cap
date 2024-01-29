#include <iostream>
#include <vector>
#include <set>

int main() {
    int n, q;
    std::cin >> n >> q;

    std::set<int> notifs;
    std::vector<int> timestamps;
    std::vector<std::vector<int>> user_timestamps(n + 1);
    int last_cleared = 0;

    for (int operation = 0; operation < q; ++operation) {
        int w, x;
        std::cin >> w >> x;

        if (w == 1) {
            timestamps.push_back(operation);
            user_timestamps[x].push_back(operation);
            notifs.insert(operation);
        } else if (w == 2) {
            for (int timestamp : user_timestamps[x]) {
                notifs.erase(timestamp);
            }
            user_timestamps[x].clear();
        } else if (w == 3) {
            while (last_cleared < x) {
                if (last_cleared < static_cast<int>(timestamps.size())) {
                    notifs.erase(timestamps[last_cleared]);
                    last_cleared++;
                } else {
                    break;
                }
            }
        }

        std::cout << notifs.size() << std::endl;
    }

    return 0;
}
