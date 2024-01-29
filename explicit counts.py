tests = int(input())

for i in range(tests):
	B = input()
	nums = B.split()
	add = int(nums[0])
	sub = int(nums[1])
	ans = 0
	for _ in range(add):
		ans += int(input())
	for _ in range(sub):
		ans -= int(input())
	print(ans)
