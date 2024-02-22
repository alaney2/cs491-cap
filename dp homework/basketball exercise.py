def max_height(n, heights_row1, heights_row2):
    if n == 1:
        return max(heights_row1[0], heights_row2[0])

    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = heights_row1[0]
    dp2[0] = heights_row2[0]

    for i in range(1, n):
        dp1[i] = heights_row1[i] + max(dp2[i - 1], dp2[i - 2] if i - 2 >= 0 else 0)
        dp2[i] = heights_row2[i] + max(dp1[i - 1], dp1[i - 2] if i - 2 >= 0 else 0)

    return max(dp1[n - 1], dp2[n - 1])

n = int(input())
heights_row1 = list(map(int, input().split()))
heights_row2 = list(map(int, input().split()))
print(max_height(n, heights_row1, heights_row2))
