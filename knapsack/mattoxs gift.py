N, S = map(int, input().split())
w = [0] * N
c = [0] * N
for i in range(N):
    w[i], c[i] = map(int, input().split())

dp = {}  # Using a dictionary as a sparse array
dp[0] = 0  # Base case

for i in range(N):
    for j in range(w[i], S + 1):
        if j in dp or (j - w[i]) in dp:
            dp[j] = max(dp.get(j, 0), dp.get(j - w[i], 0) + c[i])

print(dp.get(S, 0))