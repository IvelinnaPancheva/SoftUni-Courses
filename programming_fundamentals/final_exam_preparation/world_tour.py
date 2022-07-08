stops = input()

command = input()
while command != "Travel":
    split_data = command.split(":")
    if split_data[0] == "Add Stop":
        index = int(split_data[1])
        new_stop = split_data[2]

        if 0 <= index <= len(stops) -1:
            stops = stops[0:index] + new_stop + stops[index:]

        print(stops)

    elif split_data[0] == "Remove Stop":
        start_index = int(split_data[1])
        end_index = int(split_data[2])
        if 0 <= start_index <= end_index <= len(stops) - 1:
            stops = stops[0:start_index] + stops[(end_index+1):]
        print(stops)

    elif split_data[0] == "Switch":
        old_stop = split_data[1]
        new_stop = split_data[2]
        if old_stop in stops:
            stops = stops.replace(old_stop, new_stop)
        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")