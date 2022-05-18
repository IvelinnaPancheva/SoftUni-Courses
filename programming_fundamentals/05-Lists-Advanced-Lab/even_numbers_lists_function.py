def even_nums_indices(sequence):
    sequence = list(map(int, sequence))
    indices = []
    for index in range(len(sequence)):
        if sequence[index] % 2 == 0:
            indices.append(index)
    return indices


numbers_sequence = input().split(", ")
print(even_nums_indices(numbers_sequence))