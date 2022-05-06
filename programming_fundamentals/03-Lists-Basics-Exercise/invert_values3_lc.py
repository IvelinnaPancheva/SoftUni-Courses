def invert_values(starting_list):
    inverted_list = [int(x) for x in starting_list]
    inverted_list = [abs(x) if x <= 0 else -x for x in inverted_list]
    return inverted_list


current_starting_list = input().split(" ")
final_list = invert_values(current_starting_list)
print(final_list)