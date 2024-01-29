lines = input()
n, m = [int(x) for x in lines.split()]

d = {}
for i in range(n):
	name, ip = input().split()
	d[ip] = name

for i in range(m):
	ans = input()
	command, ip = ans.split()
	ip = ip[:-1]
	ans += f' #{d[ip]}'
	print(ans)