first_char = input()
second_char = input()
text = input()
total_sum = 0

for number in range(ord(first_char)+1, ord(second_char)):
    for char in text:
        if ord(char) == number:
            total_sum += ord(char)

print(total_sum)