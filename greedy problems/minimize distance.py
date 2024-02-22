t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()

    first_positive_idx = next((i for i, num in enumerate(x) if num >= 0), n)

    total_sum = 0
    for i in range(n - 1, first_positive_idx - 1, -k):
        total_sum += 2 * x[i]

    for i in range(0, first_positive_idx, k):
        total_sum -= 2 * x[i]

    extreme_value = max(-x[0] if first_positive_idx > 0 else 0, x[n - 1] if first_positive_idx < n else 0)
    total_sum -= extreme_value

    print(total_sum)
