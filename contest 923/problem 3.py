t = int(input())

for _ in range(t):
  n, m, k = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  half = k // 2
  if half > n or half > m:
    print('NO')
    continue
    
  a.sort()
  b.sort()
  i = 0
  j = 0
  curr = 1
  a_only = []
  b_only = []
  no = False
  while i < n and j < m and curr <= k:
    while i < n and a[i] < curr:
      i += 1
    while j < m and b[j] < curr:
      j += 1
    if i < n and j < m and a[i] == curr and b[j] == curr:
      curr += 1
      i += 1
      j += 1
    elif a[i] == curr:
      a_only.append(a[i])
      curr += 1
      i += 1
    elif b[j] == curr:
      b_only.append(b[j])
      curr += 1
      j += 1
    else:
      print('NO')
      no = True
      break
  if no:
    continue
  a_only = set(a_only)
  b_only = set(b_only)

  import bisect
  a_useful = bisect.bisect_left(a, k+1)
  b_useful = bisect.bisect_left(b, k+1)
  a_num = len(set(a[:a_useful]))
  b_num = len(set(b[:b_useful]))
  intersecting = len(a_only.intersection(b_only))
  if a_num + b_num - intersecting >= k:
    num_intersecting = 0
    yes = False
    while num_intersecting <= intersecting:
      if a_num + num_intersecting >= half and b_num + intersecting - num_intersecting >= half:
        print('YES')
        yes = True
        break
      num_intersecting += 1
    if not yes:
      print('NO')
      
  else:
    print('NO')
