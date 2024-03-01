N, S = list(map(int, input().split()))
w = [0] * N
c = [0] * N
for i in range(N):
  w[i], c[i] = list(map(int, input().split()))
  
def knapsack(w, c, item, remW):
  if item == N or remW <= 0:
    return 0
  if w[item] > remW:
    return (knapsack(w, c, item + 1, remW))
  return max(knapsack(w, c, item + 1, remW), 
             c[item] + knapsack(w, c, item + 1, remW - w[item]), 
             c[item] + knapsack(w, c, item, remW - w[item]))

print(knapsack(w, c, 0, S))
