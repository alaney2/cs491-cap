s1 = input()
s2 = input()
n = int(input())

if len(s1) != len(s2):
  print(-1)
  exit()

cost_matrix = [[float('inf') for _ in range(26)] for _ in range(26)]
for i in range(26):
  cost_matrix[i][i] = 0

for _ in range(n):
  c1, c2, cost = input().split()
  cost = int(cost)
  prev_cost = cost_matrix[ord(c1) - ord('a')][ord(c2) - ord('a')]
  cost_matrix[ord(c1) - ord('a')][ord(c2) - ord('a')] = min(prev_cost, cost)

for k in range(26):
  for i in range(26):
    for j in range(26):
      cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k][j])

cost = 0
result = []

for c1, c2 in zip(s1, s2):
    if c1 == c2:
        result.append(c1)
        continue

    min_cost = float('inf')
    best_char = None
    for c in range(26):
        intermediate_char = chr(c + ord('a'))
        cost_to_intermediate = cost_matrix[ord(c1) - ord('a')][c]
        cost_from_intermediate = cost_matrix[ord(c2) - ord('a')][c]
        total_cost = cost_to_intermediate + cost_from_intermediate

        if total_cost < min_cost:
            min_cost = total_cost
            best_char = intermediate_char

    if min_cost == float('inf'):
        print(-1)
        exit()
    else:
        cost += min_cost
        result.append(best_char)
  
print(cost)
print(''.join(result))
