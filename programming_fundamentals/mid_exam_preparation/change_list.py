num_sequence = input().split(" ")
num_sequence = list(map(int, num_sequence))
command = input().split(" ")

while True:
    if command[0] == "Delete":
        value = int(command[1])
        num_sequence = list(filter(lambda x: x if x != value else not x, num_sequence))
    elif command[0] == "Insert":
        element = int(command[1])
        position = int(command[2])
        num_sequence.insert(position, element)
    elif command[0] == "Odd":
        num_sequence = [str(x) for x in num_sequence if x % 2 != 0]
        print(" ".join(num_sequence))
        break
    elif command[0] == "Even":
        num_sequence = [str(x) for x in num_sequence if x % 2 == 0]
        print(" ".join(num_sequence))
        break
    command = input().split(" ")

