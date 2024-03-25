bacteria = int(input())

count = 0
while bacteria > 0:
  bacteria = bacteria & (bacteria - 1)
  count += 1
  
print(count)
  