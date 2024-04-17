import math

def update(block_sum, arr, left_idx, right_idx, val):

    start_block = left_idx // block_size
    end_block = right_idx // block_size
    
    if start_block == end_block:
        for i in range(left_idx, right_idx + 1):
            arr[i] += val
            block_sum[start_block] += val
    else:
        for i in range(left_idx, (start_block + 1) * block_size):
            arr[i] += val
            block_sum[start_block] += val
        for i in range(start_block + 1, end_block):
            block_sum[i] += val
        for i in range(end_block * block_size, right_idx + 1):
            arr[i] += val
            block_sum[end_block] += val
          

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
        parts = input().split()
        parts = [int(i) for i in parts]
        if parts[0] == 1:
            update(block_sum, arr, parts[1] - 1, parts[2] - 1, parts[3])
        else:
            print(query(block_sum, arr, parts[1] - 1, parts[2] - 1))

main()
