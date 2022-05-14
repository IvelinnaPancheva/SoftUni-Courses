def convert_string_to_int(list_variable):
    num_list = []
    for item in list_variable:
        num_list.append(int(item))
    return num_list


num_sequence = input().split(" ")
new_sequence = convert_string_to_int(num_sequence)
print(f"The minimum number is {min(new_sequence)}")
print(f"The maximum number is {max(new_sequence)}")
print(f"The sum number is: {sum(new_sequence)}")
