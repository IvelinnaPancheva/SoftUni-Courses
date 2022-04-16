from sys import maxsize

minimum = maxsize

command = input()

while command != "Stop":
    command = int(command)
    if command < minimum:
        minimum = command
    command = input()

print(minimum)