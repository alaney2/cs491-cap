#include <iostream>
#include <vector>
#include <set>
#include <cmath>

using namespace std;
typedef long long ll;

int main() {
    int t;
    ll hC, dC; // Health and attack of the character
    ll hM, dM; // Health and attack of the monster
    int k, w, a; // Coins, weapon upgrade, armor upgrade
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cin >> hC >> dC;

        cin >> hM >> dM;

        cin >> k >> w >> a;

        bool yes = false;
        for (int j = 0; j <= k; ++j) {
            int weapon_upgrade = w * j;
            int armor_upgrade = a * (k - j);
            ll new_hC = hC + armor_upgrade;
            ll new_dC = dC + weapon_upgrade;

            ll enemy_turns = (new_hC + dM - 1) / dM;
            ll player_turns = (hM + new_dC - 1) / new_dC;
            if (hM <= new_dC || enemy_turns >= player_turns) {
                cout << "YES" << endl;
                yes = true;
                break;
            }
        }
        if (!yes) {
            cout << "NO" << endl;
        }
    }

    return 0;
}
