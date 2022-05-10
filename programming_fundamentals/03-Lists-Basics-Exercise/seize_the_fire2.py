fire_type_string = input()
water = int(input())

total_fire = 0
effort = 0
put_out_cells= list()

list_fire_type = fire_type_string.split("#")

for fire in list_fire_type:
    if water == 0:
        break

    current_type = fire.split(" = ")[0]
    current_fire = int(fire.split(" = ")[1])

    if "High" in current_type:
        if 81 <= current_fire <= 125:
            if current_fire <= water:
                total_fire += current_fire
                water -= current_fire
                put_out_cells.append(current_fire)
                effort += 0.25 * current_fire

    if "Medium" in current_type:
        if 51 <= current_fire <= 80:
            if current_fire <= water:
                total_fire += current_fire
                water -= current_fire
                put_out_cells.append(current_fire)
                effort += 0.25 * current_fire

    if "Low" in current_type:
        if 1 <= current_fire <= 50:
            if current_fire <= water:
                total_fire += current_fire
                water -= current_fire
                put_out_cells.append(current_fire)
                current_effort = 0.25 * current_fire
                effort += 0.25 * current_fire

print("Cells:")
for element in put_out_cells:
    print(f"- {element}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")