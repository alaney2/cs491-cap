import sys

def tsp(n, beauty, price_floor):
    dp = [[float('inf')] * (1 << n) for _ in range(n)]
    dp[0][1] = 0

    for mask in range(1, 1 << n):
        if mask & 1 == 0:
            continue
        for i in range(n):
            if mask & (1 << i) == 0:
                continue
            for j in range(n):
                if i == j or mask & (1 << j) == 0:
                    continue
                cost = max(price_floor[i], beauty[j] - beauty[i])
                dp[j][mask] = min(dp[j][mask], dp[i][mask ^ (1 << j)] + cost)

    min_cost = sys.maxsize
    for i in range(1, n):
        cost = max(price_floor[i], beauty[0] - beauty[i])
        min_cost = min(min_cost, dp[i][(1 << n) - 1] + cost)

    return min_cost

n = int(input())
beauty = []
price_floor = []
for _ in range(n):
    a, c = map(int, input().split())
    beauty.append(a)
    price_floor.append(c)

print(tsp(n, beauty, price_floor))
