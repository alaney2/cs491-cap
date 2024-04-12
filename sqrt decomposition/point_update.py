import math

def update(block_sum, arr, idx, val):
    block_idx = idx // block_size
    block_sum[block_idx] += val
    arr[idx] += val

def query(block_sum, arr, l, r):
    sum = 0
    start_block = l // block_size
    end_block = r // block_size

    if start_block == end_block:
        for i in range(l, r + 1):
            sum += arr[i]
    else:
        for i in range(l, (start_block + 1) * block_size):
            sum += arr[i]
        for i in range(start_block + 1, end_block):
            sum += block_sum[i]
        for i in range(end_block * block_size, r + 1):
            sum += arr[i]
    
    return sum

def main():
    n, m = map(int, input().split())
    arr = [0] * n
    global block_size 
    block_size = int(math.sqrt(n))
    block_sum = [0] * (n // block_size + 1)

    for _ in range(m):
        t, x, y = map(int, input().split())
        if t == 1:
            update(block_sum, arr, x - 1, y)
        else:
            print(query(block_sum, arr, x - 1, y - 1))

main()