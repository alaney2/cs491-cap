def tsp(n, beauty, price_floor):
    dp = [[float('inf')] * (1 << n) for _ in range(n)]
    dp[0][1] = 0

    for mask in range(1, 1 << n):
        if mask & 1 == 0:
            continue
        for i in range(n):
            if mask & (1 << i):
                prev_mask = mask ^ (1 << i)
                for j in range(n):
                    if prev_mask & (1 << j):
                        cost = max(price_floor[j], beauty[i] - beauty[j])
                        dp[i][mask] = min(dp[i][mask], dp[j][prev_mask] + cost)

    min_cost = float('inf')
    final_mask = (1 << n) - 1
    for i in range(1, n):
        if final_mask & (1 << i):
            cost = max(price_floor[i], beauty[0] - beauty[i])
            min_cost = min(min_cost, dp[i][final_mask] + cost)

    return min_cost


n = int(input())
beauty = []
price_floor = []
for _ in range(n):
    a, c = map(int, input().split())
    beauty.append(a)
    price_floor.append(c)

min_cost = tsp(n, beauty, price_floor)
print(min_cost)
