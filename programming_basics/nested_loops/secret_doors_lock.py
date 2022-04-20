hundreds_upper_limit = int(input())
tens_upper_limit = int(input())
units_upper_limit = int(input())

for x in range(1, hundreds_upper_limit + 1):
    if x % 2 == 0:
        for y in range(1, tens_upper_limit + 1):
            if y == 2 or y == 3 or y == 5 or y == 7:
                for z in range(1, units_upper_limit + 1):
                    if z % 2 == 0:
                        print(f"{x} {y} {z}")