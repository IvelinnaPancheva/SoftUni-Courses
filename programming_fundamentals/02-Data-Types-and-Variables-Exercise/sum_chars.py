n = int(input())

sum_of_char = 0
for i in range(n):
    character = input()
    sum_of_char += ord(character)

print(f"The sum equals: {sum_of_char}")
