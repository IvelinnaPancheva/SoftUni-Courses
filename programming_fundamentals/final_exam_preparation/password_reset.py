password = input()

command = input()
while command != "Done":
    split_command = command.split(" ")
    # "TakeOdd"
    if split_command[0] == "TakeOdd":
        temporary = ""
        for index in range(len(password)):
            if index % 2 != 0:
                temporary += password[index]
        print(temporary)
        password = temporary

    # "Cut {index} {length}"
    elif split_command[0] == "Cut":
        start_index = int(split_command[1])
        length = int(split_command[2])
        end_index = start_index + length
        substring = password[start_index:end_index]
        password = password.replace(substring, "", 1)
        print(password)

    # "Substitute {substring} {substitute}"
    elif split_command[0] == "Substitute":
        old_substring = split_command[1]
        new_substring = split_command[2]
        if password.count(old_substring) != 0:
            password = password.replace(old_substring, new_substring)
            print(password)
        else: # password.count(old_substring) == 0
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")
