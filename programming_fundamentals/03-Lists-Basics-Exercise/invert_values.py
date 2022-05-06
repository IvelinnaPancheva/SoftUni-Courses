starting_string = input()

starting_list = starting_string.split(" ")
inverted_list = list()

for i in range(len(starting_list)):
    if int(starting_list[i]) > 0:
        current_number = 0 - int(starting_list[i])
        inverted_list.append(current_number)
    elif int(starting_list[i]) == 0:
        inverted_list.append(0)
    else:
        current_number = abs(int(starting_list[i]))
        inverted_list.append(current_number)

print(inverted_list)