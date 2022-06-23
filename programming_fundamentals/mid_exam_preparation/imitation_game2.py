def move_letters(text, n):
    text = text[n:] + text[0:n]
    return text


def insert_string(text, i, string):
    text = text[0:i] + string + text[i:]
    return text


def change_all(text, old_str, new_str):
    text = text.replace(old_str, new_str)
    return text


message = input()
command = input()

while command != "Decode":
    split_data = command.split('|')
    # "Move {number of letters}":
    if split_data[0] == "Move":
        n_letters = int(split_data[1])
        message = move_letters(message, n_letters)

    # "Insert {index} {value}":
    elif split_data[0] == "Insert":
        index = int(split_data[1])
        value = split_data[2]
        message = insert_string(message, index, value)

    # "ChangeAll {substring} {replacement}":
    elif split_data[0] == "ChangeAll":
        substring = split_data[1]
        replacement = split_data[2]
        message = change_all(message, substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")

