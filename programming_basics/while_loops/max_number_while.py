import sys

maximum = - sys.maxsize

command = input()

while command != "Stop":
    command = int(command)
    if command > maximum:
        maximum = command
    command = input()

print(maximum)

