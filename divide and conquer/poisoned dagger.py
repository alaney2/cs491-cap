tests = int(input())

for i in range(tests):
    temp = input().split()
    n = int(temp[0])
    h = int(temp[1])
    
    a = list(map(int, input().split()))
    
    lower = 1
    upper = h
    
    while lower < upper:
        k = (lower + upper) // 2
        damage = 0
        for j in range(len(a)-1):
            if a[j+1] - a[j] >= k:
                damage += k
            else:
                damage += a[j+1] - a[j]
        damage += k
        if damage == h:
            lower = k
            break
        if damage > h:
            upper = k
        else:
            lower = k + 1
            
    print(lower)
