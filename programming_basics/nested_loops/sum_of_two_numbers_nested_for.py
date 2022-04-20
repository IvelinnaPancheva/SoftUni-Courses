start_interval = int(input())
end_interval = int(input()) # end always > start
magic_number = int(input())

combinations_counter = 0
is_magic_combination_found = False

for number1 in range(start_interval, end_interval + 1):
    for number2 in range(start_interval, end_interval + 1):
        sum = number2 + number1
        combinations_counter += 1

        if sum == magic_number:
            is_magic_combination_found = True
            break

    if is_magic_combination_found:
        break


if is_magic_combination_found:
    print(f"Combination N:{combinations_counter} ({number1} + {number2} = {magic_number})")

else:
    print(f"{combinations_counter} combinations - neither equals {magic_number}")
