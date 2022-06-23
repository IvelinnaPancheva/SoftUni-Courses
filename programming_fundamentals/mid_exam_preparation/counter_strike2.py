initial_energy = int(input())
command = input()
win_counter = 0

while command != "End of battle":
    current_distance = int(command)
    if initial_energy >= current_distance:
        initial_energy -= current_distance
        win_counter += 1
        if win_counter % 3 == 0:
            initial_energy += win_counter
    else: # initial_energy < current_distance
        print(f"Not enough energy! Game ends with {win_counter} won battles and {initial_energy} energy")
        break
    command = input()

if command == "End of battle":
    print(f"Won battles: {win_counter}. Energy left: {initial_energy}")




