t = int(input())

for _ in range(t):
    string = list(input())
    result = 0
    if len(string) == 1:
        print(0)
        continue
      
    if string[0] == string[1]:
        result += 1
        string[1] = "0"
        
    for i in range(2, len(string)):
        if string[i] == string[i-1]:
            result += 1
            string[i] = "0"
        elif string[i] == string[i-2]:
            result += 1
            string[i] = "0"
            
    print(result)
    