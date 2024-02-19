#include <cstdio>
#include <vector>

long findSetRoot(long element, std::vector<long> &parent) {
    if (parent[element] == element) {
        return element;
    }
    return parent[element] = findSetRoot(parent[element], parent);
}

int main() {
    long n, m;
    scanf("%ld %ld", &n, &m);

    std::vector<long> parent(n + 1);
    std::vector<long> groupSize(n + 1, 1);
    for (long i = 1; i <= n; i++) {
        parent[i] = i;
    }

    while (m--) {
        long groupCount;
        scanf("%ld", &groupCount);

        if (groupCount <= 0) {
            continue;
        }

        long firstMember;
        scanf("%ld", &firstMember);
        long root = findSetRoot(firstMember, parent);

        while (--groupCount) {
            long member;
            scanf("%ld", &member);
            long memberRoot = findSetRoot(member, parent);

            if (root != memberRoot) {
                // Union of two sets
                parent[memberRoot] = root;
                groupSize[root] += groupSize[memberRoot];
            }
        }
    }

    for (long i = 1; i <= n; i++) {
        long root = findSetRoot(i, parent);
        printf("%ld ", groupSize[root]);
    }
    puts("");

    return 0;
}
