def absolute_float_values(list_of_numbers):
    for i in range(len(list_of_numbers)):
        list_of_numbers[i] = abs(float(list_of_numbers[i]))
    return  list_of_numbers

print(absolute_float_values(input().split(" ")))

