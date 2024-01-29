
low = 1
high = 10**18


guess = (low + high) // 2

print(guess)

ret = input()

while ret != 'CORRECT':
    if ret == 'HIGHER':
        low = guess + 1
    else:
        high = guess - 1

    guess = (low + high) // 2
    print(guess)
    ret = input()