def contain_substring(activation_str, substr):
    if activation_str.count(substr) != 0:
        print(f"{activation_str} contains {substr}")
    else:  # activation key doesn't contain substring
        print("Substring not found!")
    return activation_str


def flip_upper_or_lower(activation_string, method_keyword, start, end):
    if method_keyword == "Upper":
        substr = activation_string[start_index:end_index].upper()
    else: # method_keyword == "Lower":
        substr = activation_string[start_index:end_index].lower()
    activation_string = activation_string[0:start] + substr + activation_string[end:]
    print(activation_string)
    return activation_string


def slice_string(activation_string, start, end):
    activation_string = activation_key[0:start] + activation_key[end:]
    print(activation_string)
    return activation_string


activation_key = input()

command = input()

while command != "Generate":
    split_command = command.split(">>>")
    # "Contains>>>{substring}":
    if split_command[0] == "Contains":
        substring = split_command[1]
        activation_key = contain_substring(activation_key, substring)

    # "Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
    elif split_command[0] == "Flip":
        method = split_command[1]
        start_index = int(split_command[2])
        end_index = int(split_command[3])

        activation_key = flip_upper_or_lower(activation_key, method, start_index, end_index)

    # "Slice>>>{startIndex}>>>{endIndex}":
    elif split_command[0] == "Slice":
        start_index = int(split_command[1])
        end_index = int(split_command[2])
        activation_key = slice_string(activation_key, start_index, end_index)

    command = input()

print(f"Your activation key is: {activation_key}")