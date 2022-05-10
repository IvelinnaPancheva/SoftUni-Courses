fire_type_value_string = input()
water = int(input())

total_fire = 0
total_effort = 0
put_out_cells= list()
numbers_list = list()

list_fire_type_value = fire_type_value_string.split("#")
for sub in list_fire_type_value:
    current = int(sub.split("=")[1])
    numbers_list.append(current)

for i in range(len(list_fire_type_value)):
    if water == 0:
        break

    if "High" in list_fire_type_value[i]:
        if 81 <= numbers_list[i] <= 125:
            current_fire = numbers_list[i]
            if current_fire <= water:
                total_fire += current_fire
                water -= current_fire
                put_out_cells.append(current_fire)
                current_effort = 0.25 * current_fire
                total_effort += current_effort

    if "Medium" in list_fire_type_value[i]:
        if 51 <= numbers_list[i] <= 80:
            current_fire = numbers_list[i]
            if current_fire <= water:
                total_fire += current_fire
                water -= current_fire
                put_out_cells.append(current_fire)
                current_effort = 0.25 * current_fire
                total_effort += current_effort

    if "Low" in list_fire_type_value[i]:
        if 1 <= numbers_list[i] <= 50:
            current_fire = numbers_list[i]
            if current_fire <= water:
                total_fire += current_fire
                water -= current_fire
                put_out_cells.append(current_fire)
                current_effort = 0.25 * current_fire
                total_effort += current_effort
print("Cells:")
for element in put_out_cells:
    print(f"- {element}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")