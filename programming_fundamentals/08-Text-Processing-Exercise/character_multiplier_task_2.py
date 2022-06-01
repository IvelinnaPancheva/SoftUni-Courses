def character_muliplier(shorter_text, longer_text):
    total_sum = 0
    for index in range(len(shorter_text)):
        total_sum += ord(shorter_text[index]) * ord(longer_text[index])

    for ind in range(len(shorter_text), len(longer_text)):
        total_sum += ord(longer_text[ind])
    return total_sum


data = input().split(" ")
first = data[0]
second = data[1]
total = 0
if len(first) >= len(second):
    total = character_muliplier(second, first)
else: # len(first) < len(second)
    total = character_muliplier(first, second)

print(total)
