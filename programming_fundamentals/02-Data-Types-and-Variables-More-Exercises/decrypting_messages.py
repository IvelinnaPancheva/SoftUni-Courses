key = int(input())
n = int(input())
message = ""

for i in range(n):
    current_character = input()
    message += chr(ord(current_character) + key)

print(message)
