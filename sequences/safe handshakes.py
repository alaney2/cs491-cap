import math
n = int(input())

num = math.factorial(2 * n) / (math.factorial(n) * math.factorial(n+1))

print(int(num))