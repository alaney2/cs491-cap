import sys
n = int(input())

preferences = list(map(int, input().split()))
preferences = [preference - 1 for preference in preferences]
for i in range(n):
    crush = preferences[i]
    crush_of_crush = preferences[crush]
    crush_of_crush_of_crush = preferences[crush_of_crush]
    
    if crush_of_crush_of_crush == i:
        print("YES")
        sys.exit(0)
        
print("NO")
