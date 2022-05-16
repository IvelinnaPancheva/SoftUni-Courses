to_do_list = [0 for num in range(11)]
to_do_command = input().split("-")

while to_do_command[0] != "End":
    index = int(to_do_command[0])
    to_do_list.insert(index, to_do_command[1])
    to_do_command = input().split("-")

final_to_do = [x for x in to_do_list if x != 0]
print(final_to_do)