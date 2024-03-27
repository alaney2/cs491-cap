from math import gcd

def make_coprime_array(arr):
    result = [arr[0]]
    for i in range(1, len(arr)):
        num = arr[i]
        if gcd(result[-1], num) != 1:
            result.append(1)
        result.append(num)
    return result

n = int(input())
arr = list(map(int, input().split()))

coprime_arr = make_coprime_array(arr)

k = len(coprime_arr) - n
print(k)
print(*coprime_arr)
