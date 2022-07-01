def insert_space(secret_message, num):
    secret_message = secret_message[0:num] + " " + secret_message[num:]
    return secret_message


def reverse_substring(secret_message, str_to_reverse):
    secret_message = secret_message.replace(str_to_reverse, "", 1)
    str_to_reverse = str_to_reverse[::-1]
    secret_message += str_to_reverse
    return secret_message



def change_all_occurrences(secret_message, str_to_replace, new_str):
    secret_message = secret_message.replace(str_to_replace, new_str)
    return secret_message


message = input()

command = input()

while command != "Reveal":
    split_data = command.split(":|:")

    # "InsertSpace:|:{index}":
    if split_data[0] == "InsertSpace":
        index = int(split_data[1])
        message = insert_space(message, index)
        print(message)

    # "Reverse:|:{substring}":
    elif split_data[0] == "Reverse":
        substring = split_data[1]
        if substring in message:
            message = reverse_substring(message, substring)
            print(message)

        else: # substring not found in message
            print("error")

    # "ChangeAll:|:{substring}:|:{replacement}":
    elif split_data[0] == "ChangeAll":
        substring, replacement = split_data[1], split_data[2]
        if substring in message:
            message = change_all_occurrences(message, substring, replacement)
            print(message)

    command = input()

print(f"You have a new text message: {message}")