from collections import deque

liters = int(input())
dispenser_queue = deque()
name = input()
while name != "Start":
    dispenser_queue.append(name)
    name = input()
command = input()
while command != "End":
    if command.isdigit():
        needed_water = int(command)
        name = dispenser_queue.popleft()
        if liters >= needed_water:
            print(f"{name} got water" )
            liters -= needed_water
        else:
            print(f"{name} must wait")
    elif command.startswith("refill"):
        added_water = int(command.split()[1])
        liters += added_water

    command = input()
print(f"{liters} liters left")
