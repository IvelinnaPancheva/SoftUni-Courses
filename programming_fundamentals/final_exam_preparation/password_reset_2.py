def take_odd(raw_password):
    temporary = ""
    for index in range(len(raw_password)):
        if index % 2 != 0:
            temporary += raw_password[index]
    raw_password = temporary
    return raw_password


def cut_ind_len(raw_password, start, end):
    substring = raw_password[start:end]
    raw_password = raw_password.replace(substring, "", 1)
    return raw_password


def substitute_strings(raw_password, old, new):
    if raw_password.count(old) != 0:
        raw_password = raw_password.replace(old, new)
        print(raw_password)
        return raw_password
    else:  # password.count(old_substring) == 0
        print("Nothing to replace!")
        return raw_password


password = input()

command = input()
while command != "Done":
    split_command = command.split(" ")
    # "TakeOdd"
    if split_command[0] == "TakeOdd":
        password = take_odd(password)
        print(password)

    # "Cut {index} {length}"
    elif split_command[0] == "Cut":
        start_index = int(split_command[1])
        length = int(split_command[2])
        end_index = start_index + length
        password = cut_ind_len(password, start_index, end_index)
        print(password)

    # "Substitute {substring} {substitute}"
    elif split_command[0] == "Substitute":
        old_substring = split_command[1]
        new_substring = split_command[2]
        password = substitute_strings(password, old_substring, new_substring)

    command = input()

print(f"Your password is: {password}")
