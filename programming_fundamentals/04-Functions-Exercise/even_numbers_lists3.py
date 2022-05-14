numbers_sequence = input().split(", ")
numbers_sequence = list(map(int, numbers_sequence))
indices = []

indices = list(map(lambda x: x if numbers_sequence[x] % 2 == 0 else "no", range(len(numbers_sequence))))
even_indices = list(filter(lambda x: x != "no", indices))

print(even_indices)