def rounding_function(numbers_list):
    for index in range(len(numbers_list)):
        numbers_list[index] = round(float(numbers_list[index]))
    return numbers_list


float_sequence = input().split(" ")
print(rounding_function(float_sequence))