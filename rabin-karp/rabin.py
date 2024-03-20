d = 256
D = 512
Q = 10007

def search(pattern, text, q):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    P = 0
    T = 0
    hhhhh = 1
    HH = 1
    i = 0
    j = 0

    count = 0
    for i in range(m-1):
        hhhhh = (hhhhh*d) % q
        HH = (HH*D) % Q

    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
        P = (D*P + ord(pattern[i])) % Q
        T = (D*T + ord(text[i])) % Q

    # Find the match
    for i in range(n-m+1):
        if p == t and P == T:
            count += 1

        if i < n-m:
            t = (d*(t-ord(text[i])*hhhhh) + ord(text[i+m])) % q
            T = (D*(T-ord(text[i])*HH) + ord(text[i+m])) % Q
            
            if t < 0:
                t = t+q
            if T < 0:
                T = T+Q
                
    print(count)


text = input()
pattern = input()
if len(pattern) > len(text):
    print(0)
    exit()
q = 100003
search(pattern, text, q)