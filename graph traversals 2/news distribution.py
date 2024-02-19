def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
group_size = [1] * (n + 1)

for _ in range(m):
    group = list(map(int, input().split()))
    if len(group) <= 1:
        continue

    roots = {find(member, parent) for member in group[1:group[0]+1]}

    main_root = max(roots, key=lambda x: group_size[x])
    for r in roots:
        if main_root != r:
            if group_size[main_root] < group_size[r]:
                main_root, r = r, main_root
            parent[r] = main_root
            group_size[main_root] += group_size[r]

for i in range(1, n + 1):
    root = find(i, parent)
    print(group_size[root], end=" ")
print()
