numbers_sequence = input().split(", ")
numbers_sequence = list(map(int, numbers_sequence))
indices = []

for index in range(len(numbers_sequence)):
    if numbers_sequence[index] % 2 == 0:
        indices.append(index)

print(indices)