t = int(input())

for _ in range(t):
    n, B, x, y = map(int, input().split())
    a = [0] * (n+1)
    for i in range(1, len(a)):
        if a[i-1] + x <= B:
            a[i] = a[i-1] + x
        else:
            a[i] = a[i-1] - y
    print(sum(a))