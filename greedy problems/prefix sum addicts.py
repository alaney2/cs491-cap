tests = int(input())

for _ in range(tests):
    n, k = map(int, input().split())
    prefix_sums = [0] * (n + 1)
    prefix_sums[n - k + 1:] = list(map(int, input().split()))
    
    if k == 1:
        print("YES")
        continue

    a = [0] * (n + 1)
    for i in range(n - k + 2, n + 1):
        a[i] = prefix_sums[i] - prefix_sums[i - 1]

    if sorted(a[n - k + 2:]) != a[n - k + 2:]:
        print("NO")
        continue

    if prefix_sums[n - k + 1] > a[n - k + 2] * (n - k + 1):
        print("NO")
        continue

    print("YES")
