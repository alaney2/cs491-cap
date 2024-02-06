t = int(input())

for _ in range(t):
  chars = int(input())
  string = str(input())
  
  left = None
  right = None
  for i, char in enumerate(string):
    if char == 'B' and left is None:
      left = i
    if char == 'B' and left is not None:
      right = i
  
  print(right - left + 1 if left is not None and right is not None else 0)