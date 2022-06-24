def find_the_longest_sequence(sequence):
    temporary = []
    max_length = 0
    longest_sequence = []
    for index in range(len(sequence) - 1, -1, -1):
        if index == len(sequence) - 1:
            temporary.append(sequence[index])
        else:  # every index but the last one
            if sequence[index] not in temporary:
                temporary.clear()
                temporary.append(sequence[index])
            else:  # sequence[index] in temporary
                temporary.append(sequence[index])
            if len(temporary) >= max_length:
                max_length = len(temporary)
                longest_sequence = temporary.copy()
    return longest_sequence


current_sequence = input().split(" ")
current_longest_sequence = find_the_longest_sequence(current_sequence)
print(" ".join(current_longest_sequence))