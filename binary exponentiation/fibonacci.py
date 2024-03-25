import numpy as np

t, m = map(int, input().split())
for _ in range(t):
    n = int(input())

    def multiply(a, b):
        c = np.dot(a, b)
        c %= m
        return c

    def power(a, n):
        if n == 1:
            return a
        if n % 2 == 0:
            return power(multiply(a, a), n // 2)
        return multiply(a, power(multiply(a, a), n // 2))

    def fibonacci(n):
        if n == 0 or n == 1:
            return 1
        return power(np.array([[1, 1], [1, 0]], dtype=object), n)[0, 0]

    print(fibonacci(n) % m)