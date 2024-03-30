def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

t = int(input())
for _ in range(t):
    n = int(input())
    gcd_, max_ = 0, 0
    arr = input().split()
    arr = [int(x) for x in arr]
    for num in arr:
        gcd_ = gcd(gcd_, num)
        max_ = max(max_, num)
    print(max_ // gcd_)
    