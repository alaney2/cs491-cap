tests = int(input())

for i in range(tests):
    x = int(input())
    if x == 1:
        print(3)
        continue
    if x % 2 == 1:
        print(1)
        continue
    
    binary = bin(x)[2:]
    flag = False
    for i, c in enumerate(binary[::-1]):
        if i == len(binary) - 1:
            break
        if c == '1':
            result = '1' + '0'*i
            print(int(result, 2))
            flag = True
            break
    if not flag:
        print(x + 1)
