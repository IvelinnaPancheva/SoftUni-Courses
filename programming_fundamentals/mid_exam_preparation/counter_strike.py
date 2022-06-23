initial_energy = int(input())
command = input()
win_counter = 0
is_there_no_energy = False

while command != "End of battle":
    current_distance = int(command)
    if initial_energy >= current_distance:
        initial_energy -= current_distance
        win_counter += 1
        if win_counter % 3 == 0:
            initial_energy += win_counter
    else: # initial_energy < current_distance
        is_there_no_energy = True
        break
    command = input()

if command == "End of battle":
    print(f"Won battles: {win_counter}. Energy left: {initial_energy}")
if is_there_no_energy:
    print(f"Not enough energy! Game ends with {win_counter} won battles and {initial_energy} energy")



