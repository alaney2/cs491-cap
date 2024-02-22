def max_score(a):
    n = len(a)
    dp = [0] * n

    for i in range(n-1, -1, -1):
        if i + a[i] < n:
            dp[i] = a[i] + dp[i + a[i]]
        else:
            dp[i] = a[i]

    return max(dp)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(max_score(a))