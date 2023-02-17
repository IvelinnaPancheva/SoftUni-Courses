def float_values_counter(numbers):
    numbers_as_dict = dict()
    for num in numbers:
        if num not in numbers_as_dict:
            numbers_as_dict[num] = 0
        numbers_as_dict[num] += 1
    for occurrence in numbers_as_dict.items():
        print(f"{occurrence[0]:.1f} - {occurrence[1]} times")


current_numbers = [float(x) for x in input().split()]
float_values_counter(current_numbers)



