N = 26
n = int(input())

parent = list(range(N))
char_in_password = [False] * N

for _ in range(n):
    password = input()
    current_password_chars = [False] * N

    for char in password:
        index = ord(char) - ord('a')
        char_in_password[index] = current_password_chars[index] = True

    first_connected_char = None
    for i in range(N):
        if current_password_chars[i]:
            first_connected_char = parent[i]
    #         parent[i] = next(parent[i] for i in range(N) if current_password_chars[i])
    # first_connected_char = next(parent[i] for i in range(N) if current_password_chars[i])
    # print('first', first_connected_char)
    
    # Union
    for i in range(N):
        if current_password_chars[i]:
            parent[parent[i]] = first_connected_char
            parent[i] = first_connected_char

distinct_classes_count = sum(char_in_password[i] and parent[i] == i for i in range(N))

print(distinct_classes_count)
