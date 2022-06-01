text = input()

element = ""
for char in text:
    if 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
        element += char
    else:
        element += "."

text = element.split(".")
text = [x for x in text if x != ""]

position = 0
total_sum = 0

for element in text:
    if len(element) >= 3:
        first_letter = element[0]
        second_letter = element[-1]
        num = int(element[1:(len(element)-1)])
        if first_letter.isupper():
            position = ord(first_letter.lower()) - 96
            num /= position
        else: # first_letter.islower():
            position = ord(first_letter) - 96
            num *= position
        if second_letter.isupper():
            position = ord(second_letter.lower()) - 96
            num -= position

        else: # second_letter.islower():
            position = ord(second_letter) - 96
            num += position

        total_sum += num

print(f"{total_sum:.2f}")