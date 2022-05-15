def data_type_action(command, data):
    if command == "int":
        return int(data) * 2
    elif command == "real":
        return f"{(float(data) * 1.5):.2f}"
    elif command == "string":
        return f"${data}$"


current_command = input()
current_string = input()
print(data_type_action(current_command, current_string))