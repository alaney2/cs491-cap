while True:
	try:
		temp = input()
		if temp is None or len(temp) == 0:
			break
		temp = temp.split()
		add = int(temp[0])
		sub = int(temp[1])
		ans = 0
		for _ in range(add):
			ans += int(input())
		for _ in range(sub):
			ans -= int(input())
		print(ans)
	except EOFError:
		break