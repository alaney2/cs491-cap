#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        vector<int> child(n + 1, 0);
        
        int result = 0;
        int parent;
        for (int i = 1; i < n; ++i) {
            cin >> parent;
            child[parent]++;
        }
        
        priority_queue<int> q1;
        vector<int> temp_storage;
        
        for (int i = 1; i <= n; ++i){
            if (child[i] > 0) {
                q1.push(child[i]);
            }
        }
        q1.push(1);
        
        int future_turns = q1.size();
        while (!q1.empty()){
            result++;
            if ((q1.top() - (future_turns)) > 0){
                temp_storage.push_back(q1.top() - future_turns);
            }
            q1.pop();
            future_turns--;
        }
        
        while (!temp_storage.empty()) {
            q1.push(temp_storage.back());
            temp_storage.pop_back();
        }
        
        while (!q1.empty()) {
            result++;
            
            if (q1.top() - 2 > 0) {
                temp_storage.push_back(q1.top() - 2);
            }
            q1.pop();
            
            while (!q1.empty()) {
                if (q1.top() - 1 > 0) {
                    temp_storage.push_back(q1.top() - 1);
                }
                q1.pop();
            }
            
            while (!temp_storage.empty()) {
                q1.push(temp_storage.back());
                temp_storage.pop_back();
            }
        }
        cout << result << "\n";
    }
}