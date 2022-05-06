def invert_values(starting_list):
    inverted_list = [abs(int(x)) if int(x) <= 0 else -int(x) for x in starting_list]
    return inverted_list


current_starting_list = input().split(" ")
final_list = invert_values(current_starting_list)
print(final_list)