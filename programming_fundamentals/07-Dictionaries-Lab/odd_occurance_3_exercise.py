sequence = input().split(" ")
chars_occurrence = dict()
sequence = [char.lower() for char in sequence]
for element in sequence:
    chars = element.lower()

    if chars not in chars_occurrence:
        chars_occurrence[chars] = 1
    else:  # if chars exist as a key in the dictionary already with a value
        chars_occurrence[chars] += 1

for char in chars_occurrence.keys():
    if chars_occurrence[char] % 2 != 0:
        print(f"{char}", end=" ")