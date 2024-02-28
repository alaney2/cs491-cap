s = input()
t = input()

arr = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

for i in range(len(s) + 1):
    arr[i][0] = i

for i in range(len(t) + 1):
    arr[0][i] = i

for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        if s[i - 1] == t[j - 1]:
            arr[i][j] = arr[i - 1][j - 1]
        else:
            arr[i][j] = min(arr[i - 1][j - 1], arr[i - 1][j], arr[i][j - 1]) + 1

print(arr[len(s)][len(t)])