def invert_values(starting_list):
    inverted_list = list()
    for i in range(len(starting_list)):
        if int(starting_list[i]) > 0:
            inverted_list.append(-int(starting_list[i]))
        else:
            inverted_list.append(abs(int(starting_list[i])))

    return inverted_list


current_starting_list = input().split(" ")
final_list = invert_values(current_starting_list)
print(final_list)