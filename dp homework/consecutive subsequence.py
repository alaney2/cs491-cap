def find_longest_consecutive_subsequence(arr):
    n = len(arr)
    longest_seq_end = {}
    max_length = -1
    pos = -1

    for i in range(n):
        count = 1 + longest_seq_end.get(arr[i] - 1, 0)
        longest_seq_end[arr[i]] = max(longest_seq_end.get(arr[i], 0), count)

        if longest_seq_end[arr[i]] > max_length:
            max_length = longest_seq_end[arr[i]]
            pos = i

    result_indices = []
    current_val = arr[pos]
    for i in range(n - 1, -1, -1):
        if arr[i] == current_val:
            result_indices.append(i + 1)
            current_val -= 1

    print(max_length)
    print(" ".join(map(str, reversed(result_indices))))


n = int(input())
arr = list(map(int, input().split()))
find_longest_consecutive_subsequence(arr)
