def first_letter_check(char, number):
    position = ord(char.lower()) - 96
    if char.isupper():
        number /= position
    else:  # first_letter.islower():
        number *= position
    return number


def last_letter_check(char, number):
    position = ord(second_letter.lower()) - 96
    if char.isupper():
        number -= position
    else: # second_letter.islower():
        number += position
    return number


text = input().split()

total_sum = 0

for element in text:
    first_letter = element[0]
    second_letter = element[-1]
    num = int(element[1:(len(element)-1)])
    num = first_letter_check(first_letter, num)
    num = last_letter_check(second_letter, num)
    total_sum += num

print(f"{total_sum:.2f}")