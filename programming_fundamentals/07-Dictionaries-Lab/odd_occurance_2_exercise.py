chars_occurrence = dict()
sequence = [char.lower() for char in input().split(" ")]
for element in sequence:
    count = 1

    if element not in chars_occurrence:
        chars_occurrence[element] = count
    else:  # if chars exist as a key in the dictionary already with a value
        chars_occurrence[element] += count

for char in chars_occurrence.keys():
    if chars_occurrence[char] % 2 != 0:
        print(f"{char}", end=" ")