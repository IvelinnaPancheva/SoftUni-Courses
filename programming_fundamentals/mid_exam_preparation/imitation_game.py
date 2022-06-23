message = input()
command = input()

while command != "Decode":
    split_data = command.split('|')
    # "Move {number of letters}":
    if split_data[0] == "Move":
        n_letters = int(split_data[1])
        substring = message[0:n_letters]
        message = message[n_letters:] + substring

    # "Insert {index} {value}":
    elif split_data[0] == "Insert":
        index = int(split_data[1])
        value = split_data[2]
        message = message[0:index] + value + message[index:]

    # "ChangeAll {substring} {replacement}":
    elif split_data[0] == "ChangeAll":
        substring = split_data[1]
        replacement = split_data[2]
        message = message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")

