def invert_values(starting_list):
    starting_list = list(map(int, starting_list))
    inverted_list = list(map(lambda x: -x if x > 0 else abs(x), starting_list))
    return inverted_list


current_starting_list = input().split(" ")
final_list = invert_values(current_starting_list)
print(final_list)