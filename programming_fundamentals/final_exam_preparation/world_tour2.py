def add_stops(string, i, new_string):
    if 0 <= i <= len(string) - 1:
        string = string[0:i] + new_string + string[i:]
    print(string)
    return string


def remove_stops(string, start, end):
    if 0 <= start <= end <= len(string) - 1:
        string = string[0:start] + string[(end + 1):]
    print(string)
    return string


def switch_stops(string, substring, new):
    if substring in string:
        string = string.replace(substring, new)
    print(string)
    return string


stops = input()

command = input()
while command != "Travel":
    split_data = command.split(":")
    if split_data[0] == "Add Stop":
        index = int(split_data[1])
        new_stop = split_data[2]
        stops = add_stops(stops, index, new_stop)

    elif split_data[0] == "Remove Stop":
        start_index = int(split_data[1])
        end_index = int(split_data[2])
        stops = remove_stops(stops, start_index, end_index)

    elif split_data[0] == "Switch":
        old_stop = split_data[1]
        new_stop = split_data[2]
        stops = switch_stops(stops, old_stop, new_stop)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")