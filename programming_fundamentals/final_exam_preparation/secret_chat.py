message = input()

command = input()

while command != "Reveal":
    split_data = command.split(":|:")

    # "InsertSpace:|:{index}":
    if split_data[0] == "InsertSpace":
        index = int(split_data[1])
        message = message[0:index] + " " + message[index:]
        print(message)

    # "Reverse:|:{substring}":
    elif split_data[0] == "Reverse":
        substring = split_data[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            substring = substring[::-1]
            message += substring
            print(message)

        else: # substring not found in message
            print("error")

    # "ChangeAll:|:{substring}:|:{replacement}":
    elif split_data[0] == "ChangeAll":
        substring, replacement = split_data[1], split_data[2]
        if substring in message:
            message = message.replace(substring, replacement)
            print(message)

    command = input()

print(f"You have a new text message: {message}")