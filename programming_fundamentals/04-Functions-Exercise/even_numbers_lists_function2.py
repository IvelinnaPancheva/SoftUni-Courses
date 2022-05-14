def even_nums_indices(sequence):
    sequence = [int(x) for x in sequence]
    indices = []
    for index in range(len(sequence)):
        if sequence[index] % 2 == 0:
            indices.append(index)
    return indices


numbers_sequence = input().split(", ")
print(even_nums_indices(numbers_sequence))