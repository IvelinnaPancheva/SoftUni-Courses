wagons = int(input())
train = [0 for i in range(wagons)]
command = input()

while command != "End":
    list_of_command = command.split(" ")
    if list_of_command[0] == "add":
        train[-1] += int(list_of_command[1])
    elif list_of_command[0] == "insert":
        index = int(list_of_command[1])
        train[index] += int(list_of_command[2])
    elif list_of_command[0] == "leave":
        index = int(list_of_command[1])
        train[index] -= int(list_of_command[2])
    command = input()

print(train)