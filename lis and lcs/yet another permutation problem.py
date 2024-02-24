def lis(nums):
    sub = []
    for num in nums:
        pos = binary_search(sub, num)
        if pos == len(sub):
            sub.append(num)
        else:
            sub[pos] = num
    return len(sub)

def binary_search(sub, num):
    left, right = 0, len(sub) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if sub[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return left


t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    position_map = {num: i for i, num in enumerate(arr2)}
    transformed_A = [position_map[num] for num in arr1]
    lis_length = lis(transformed_A)
    print(2 * n - 2 * lis_length)
