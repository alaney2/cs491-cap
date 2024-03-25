MOD = 10**9 + 7

def binExp(a, n):
    res = 1
    while n > 0:
        if n & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        n >>= 1
    return res

def solve(A, B, n, x):
    An = binExp(A, n)
    sum = (An - 1 + MOD) % MOD
    if A != 1:
        sum = (sum * binExp(A - 1, MOD - 2)) % MOD

    result = (An * x + sum * B) % MOD
    return result

A, B, n, x = map(int, input().split())

result = solve(A, B, n, x)
print(result)
