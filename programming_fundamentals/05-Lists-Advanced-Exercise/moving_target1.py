def shoot_target_in_list(list_targets,ind, num):
    list_targets[ind] -= num
    if list_targets[ind] <= 0:
        list_targets.pop(ind)
    return list_targets


def add_targe_to_list(list_targets,ind, num):
    list_targets.insert(ind, num)
    return list_targets


def strike_a_target(list_targets,ind, num):
    for i in range(len(list_targets)-1, -1, -1):
        if ind - num <= i <= ind + num:
            list_targets.pop(i)
    return list_targets


targets = input().split(" ")
targets = [int(num) for num in targets]  # list(map(int, targets))
command = input().split(" ")

while command[0] != "End":
    index = int(command[1])
    value = int(command[2])
    if command[0] == "Shoot":
        if 0 <= index <= len(targets) - 1:
            shoot_target_in_list(targets,index, value)

    elif command[0] == "Add":
        if 0 <= index <= len(targets) - 1:
            add_targe_to_list(targets, index, value)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        if 0 <= index - value <= index + value <= len(targets) - 1:
            strike_a_target(targets, index, value)
        else:
            print("Strike missed!")

    command = input().split(" ")

targets = list(map(str, targets))

print("|".join(targets))

