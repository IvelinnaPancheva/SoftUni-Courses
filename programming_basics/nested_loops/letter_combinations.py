start_letter = input()
end_letter = input()
exclude_letter = input()

start_range = ord(start_letter)
end_range = ord(end_letter)
exclude_number = ord(exclude_letter)
combinations_count = 0

for x in range(start_range, end_range + 1):
    for y in range(start_range, end_range + 1):
        for z in range(start_range, end_range + 1):
            if x != exclude_number and y != exclude_number and z != exclude_number:
                a = chr(x)
                b = chr(y)
                c = chr(z)
                print(f"{a}{b}{c}", end= " ")
                combinations_count += 1
print(combinations_count)
