activation_key = input()

command = input()

while command != "Generate":
    split_command = command.split(">>>")
    # "Contains>>>{substring}":
    if split_command[0] == "Contains":
        substring = split_command[1]
        if activation_key.count(substring) != 0:
            print(f"{activation_key} contains {substring}")
        else: # activation key doesn't contain substring
            print("Substring not found!")
    # "Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
    elif split_command[0] == "Flip":
        method = split_command[1]
        start_index = int(split_command[2])
        end_index = int(split_command[3])

        if method == "Upper":
            substring = activation_key[start_index:end_index].upper()
        else:  # method == Lower
            substring = activation_key[start_index:end_index].lower()
        activation_key = activation_key[0:start_index] + substring + activation_key[end_index:]
        print(activation_key)

    # "Slice>>>{startIndex}>>>{endIndex}":
    elif split_command[0] == "Slice":
        start_index = int(split_command[1])
        end_index = int(split_command[2])

        activation_key = activation_key[0:start_index] + activation_key[end_index:]
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")