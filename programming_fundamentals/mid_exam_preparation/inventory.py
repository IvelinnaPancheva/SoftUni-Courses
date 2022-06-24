items_list = input().split(", ")

while True:
    command = input().split(" - ")
    if command[0] == "Craft!":
        break

    else:
        if command[0] == "Collect":
            if command[1] not in items_list:
                items_list.append(command[1])
        elif command[0] == "Drop":
            if command[1] in items_list:
                items_list.remove(command[1])
        elif "Combine" in command[0]:
            items_combination = command[1].split(":")
            if items_combination[0] in items_list:
                index = items_list.index(items_combination[0])
                items_list.insert(index+1, items_combination[1])
        elif command[0] == "Renew":
            if command[1] in items_list:
                items_list.remove(command[1])
                items_list.append(command[1])

print(", ".join(items_list))