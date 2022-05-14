def sorted_function(list_variable):
    num_list = []
    for item in list_variable:
        num_list.append(int(item))
    return sorted(num_list)


num_sequence = input().split(" ")
new_sequence = sorted_function(num_sequence)
print(new_sequence)