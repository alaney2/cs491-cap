n, a, b, p, q = map(int, input().split())
a_multiple = n // a
b_multiple = n // b

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
  
lcm = (a * b) // gcd(a, b)
chocolates = p * (a_multiple) + q * (b_multiple) - (min(p, q) * (n // lcm))

print(chocolates)