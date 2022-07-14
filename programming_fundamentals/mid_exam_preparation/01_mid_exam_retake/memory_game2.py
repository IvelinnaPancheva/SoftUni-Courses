sequence = input().split(" ")
command = input()
moves_counter = 0

while "end" not in command:

    moves_counter += 1
    first_index = int(command.split(" ")[0])
    second_index = int(command.split(" ")[1])

    if first_index == second_index or first_index < 0 or second_index < 0 \
    or first_index > len(sequence) - 1 or second_index > len(sequence) - 1:
        new_element = f"-{moves_counter}a"
        sequence.insert(len(sequence)//2, new_element)
        sequence.insert(len(sequence)//2, new_element)
        print("Invalid input! Adding additional elements to the board")

    elif 0 <= first_index <= len(sequence) - 1 and 0 <= second_index <= len(sequence) - 1:
        if sequence[first_index] == sequence[second_index]:
            current = sequence[second_index]
            print(f"Congrats! You have found matching elements - {sequence[first_index]}!")
            sequence = [x for x in sequence if x != current]

        else:
            print("Try again!")
    if len(sequence) == 0:
        print(f"You have won in {moves_counter} turns!")
        break

    command = input()

if len(sequence) > 0:
    print(f"Sorry you lose :(\n{' '.join(sequence)}")
