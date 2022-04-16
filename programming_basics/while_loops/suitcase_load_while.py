total_capacity = float(input())

suitcase_counter = 0
loaded_suitcases_counter = 0
free_capacity_left_in_compartment = True
command = input()

while total_capacity > 0:
    if command == "End":
        break
    else:
        current_load = float(command)
        suitcase_counter += 1
        if suitcase_counter % 3 == 0:
            current_load += 0.1 * current_load
        total_capacity -= current_load
        if total_capacity > 0:
            loaded_suitcases_counter += 1
        else:
            free_capacity_left_in_compartment = False
            break
    command = input()

if free_capacity_left_in_compartment:
    print(f"Congratulations! All suitcases are loaded!")
    print(f"Statistic: {loaded_suitcases_counter} suitcases loaded.")
else:
    print(f"No more space!")
    print(f"Statistic: {loaded_suitcases_counter} suitcases loaded.")