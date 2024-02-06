t = int(input())

for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  result = ''
  letters = [0] * n
  for num in arr:
    result += chr(ord('a') + letters[num])
    letters[num] += 1
  print(result)
