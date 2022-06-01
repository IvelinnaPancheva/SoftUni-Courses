text = input().split()

position = 0
total_sum = 0

for element in text:
    first_letter = element[0]
    second_letter = element[-1]
    num = int(element[1:(len(element)-1)])
    position = ord(first_letter.lower()) - 96
    if first_letter.isupper():
        num /= position
    else: # first_letter.islower():
        num *= position

    position = ord(second_letter.lower()) - 96
    if second_letter.isupper():
        num -= position
    else: # second_letter.islower():
        position = ord(second_letter) - 96
        num += position

    total_sum += num

print(f"{total_sum:.2f}")