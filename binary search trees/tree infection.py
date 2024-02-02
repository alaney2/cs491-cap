from collections import Counter

tests = int(input())

for _ in range(tests):
  n = int(input())
  nodes = list(map(int, input().split()))
  counter = Counter(nodes)
  counts = list(counter.values())
  counts.sort(reverse=True)
  counts.append(1)
  
  turns = 0
  for i in range(len(counts)):
    counts[i] -= 1
    for j in range(i):
      counts[j] -= 1
    turns += 1
    while counts and counts[-1] <= 0:
      counts.pop()
  
  max_idx = 0
  while counts:
    counts[max_idx] -= 1
    if len(counts) > 1 and counts[max_idx] < counts[max_idx + 1]:
      max_idx += 1
    
    for i in range(len(counts)):
      counts[i] -= 1
    while counts and counts[-1] <= 0:
      counts.pop()
    turns += 1
    
  print(turns)
  