def query(x):
    if 1 <= x <= n and arr[x] == 0:
        print(f"? {x}", flush=True)
        arr[x] = int(input())

n = int(input())
arr = [0] * (n + 2)
arr[0] = arr[n + 1] = float('inf')

i, j = 1, n
while i <= j:
    m = (i + j) // 2
    query(m)
    query(m - 1)
    query(m + 1)

    if arr[m] < arr[m - 1] and arr[m] < arr[m + 1]:
        break
    elif arr[m] > arr[m - 1]:
        j = m - 1
    else:
        i = m + 1

print(f"! {m}", flush=True)
