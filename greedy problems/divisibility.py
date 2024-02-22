t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    
    cnt = 0
    indices = []
    for i, x in enumerate(array):
        while x > 0 and x % 2 == 0:
            cnt += 1
            x //= 2
        idx = i + 1
        idx_count = 0
        while idx > 0 and idx % 2 == 0:
            idx //= 2
            idx_count += 1
        if idx_count > 0:
            indices.append(idx_count)
    
    printed = False
    if cnt >= n:
        print(0)
        printed = True
        continue
    indices.sort()
    ans = 0
    for i in range(n, 0, -1):
        if printed:
          break
        if not indices:
            break
        cnt += indices.pop()
        ans += 1
        if cnt >= n:
            print(ans)
            printed = True
            break

    if not printed:
      print(-1)
  