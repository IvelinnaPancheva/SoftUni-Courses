def print_unique_names(n):
    unique_names = set()
    for _ in range(n):
        name = input()
        unique_names.add(name)

    print('\n'.join(unique_names))


num = int(input())
print_unique_names(n=num)
