num_sequence = input().split(", ")
sequence_of_reversed = []
for item in num_sequence:
    current = ""
    for i in range(len(item)-1, -1, -1):
        current += item[i]
    sequence_of_reversed.append(current)

for index in range(len(num_sequence)):
    if num_sequence[index] == sequence_of_reversed[index]:
        print("True")
    else:
        print("False")