n = int(input())

times = []
end_times = []
prices = []

for _ in range(n):
  t, d, p = map(int, input().split())
  times.append(t)
  end_times.append(d)
  prices.append(p)

intervals = list(zip(times, end_times, prices, range(1, n+1)))
intervals.sort(key=lambda x: x[1])

max_time = max(end_times)
dp = [[0 for _ in range(max_time + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, max_time + 1):
    if intervals[i-1][0] < j and j <= intervals[i-1][1]:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-intervals[i-1][0]] + intervals[i-1][2])
    else:
      dp[i][j] = dp[i-1][j]

max_price = dp[n][max_time]

included_items = []
i, j = n, max_time
while i > 0 and j > 0:
    if dp[i][j] != dp[i-1][j]:
        included_items.append(intervals[i-1][3])
        j -= intervals[i-1][0]
    i -= 1

included_items.reverse()
print(max_price)
print(len(included_items))
print(' '.join(map(str, included_items)))
