n, a, b, p, q = map(int, input().split())

a_multiple = n // a
b_multiple = n // b
common_multiple = n // (a * b)

chocolates = 0

if (p > q):
  chocolates = (a_multiple * p) + (b_multiple * q) - (common_multiple * q)
else:
  chocolates = (a_multiple * p) + (b_multiple * q) - (common_multiple * p)
  
print(chocolates)
