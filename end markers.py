while True:
	temp = input()
	temp = temp.split()
	add = int(temp[0])
	sub = int(temp[1])
	if add == 0 and sub == 0:
		break
	ans = 0
	for _ in range(add):
		ans += int(input())
	for _ in range(sub):
		ans -= int(input())
	print(ans)

