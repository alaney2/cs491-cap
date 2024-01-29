tests = int(input())
for i in range(tests):
	arr_len = int(input())
	arr = [int(num) for num in input().split()]

	max_beauty = float('-inf')
	arr.sort()
	max_beauty = arr[-1] + arr[-2] - arr[0] - arr[1]

	print(max_beauty)