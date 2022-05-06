starting_string = input()

starting_list = starting_string.split(" ")
inverted_list = list()

for i in range(len(starting_list)):
    if int(starting_list[i]) > 0:
        inverted_list.append(-int(starting_list[i]))

    else:
        inverted_list.append(abs(int(starting_list[i])))

print(inverted_list)