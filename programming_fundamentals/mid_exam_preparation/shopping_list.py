shopping_list = input().split("!")
command = input()

while command != "Go Shopping!":
    current_command = command.split(" ")
    if current_command[0] == "Urgent":
        if current_command[1] not in shopping_list:
            shopping_list.insert(0, current_command[1])
    elif current_command[0] == "Unnecessary":
        if current_command[1] in shopping_list:
            shopping_list.remove(current_command[1])
    elif current_command[0] == "Correct":
        if current_command[1] in shopping_list:
            index = shopping_list.index(current_command[1])
            shopping_list[index] = current_command[2]
    elif current_command[0] == "Rearrange":
        if current_command[1] in shopping_list:
            shopping_list.remove(current_command[1])
            shopping_list.append(current_command[1])
    command = input()

output_list = ", ".join(shopping_list)
print(output_list)