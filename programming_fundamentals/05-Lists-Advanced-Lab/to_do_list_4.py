to_do_list = [0 for x in range(10)]
to_do_command = input().split("-")

while to_do_command[0] != "End":
    index = int(to_do_command[0]) - 1
    to_do_list[index] = to_do_command[1]
    to_do_command = input().split("-")

final_to_do = [x for x in to_do_list if x != 0]
print(final_to_do)