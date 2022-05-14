def convert_string_to_int(list_variable):
    num_list = []
    for item in list_variable:
        num_list.append(int(item))
    return num_list


def minimum(list_variable):
    return min(list_variable)


def maximum(list_variable):
    return max(list_variable)


def sum_of_items(list_variable):
    return sum(list_variable)


num_sequence = input().split(" ")
print(f"The minimum number is {minimum(convert_string_to_int(num_sequence))}")
print(f"The maximum number is {maximum(convert_string_to_int(num_sequence))}")
print(f"The sum number is: {sum_of_items(convert_string_to_int(num_sequence))}")
