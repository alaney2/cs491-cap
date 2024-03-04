n = int(input())

times = []
end_times = []
prices = []

for _ in range(n):
  t, d, p = map(int, input().split())
  times.append(t)
  end_times.append(d)
  prices.append(p)
  
intervals = list(zip(times, end_times, prices))
intervals.sort(key=lambda x: x[1])

dp = [0] * (n + 1)

for i in range(n):
  t, d, p = intervals[i]
  dp[i + 1] = max(dp[i + 1], dp[i])
  j = i + 1
  while j < n and intervals[j][0] < d:
    j += 1
  dp[j] = max(dp[j], dp[i] + p)
  
print(dp[n])