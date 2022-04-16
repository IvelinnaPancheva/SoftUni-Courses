months = int(input())


average_e = 0
total_water = 0
total_internet = 0
total_electricity = 0
total_other = 0
total = 0

for bills in range(1, months + 1):
    electricity = float(input())
    total_electricity += electricity
    total_water += 20
    total_internet += 15
    total_other += (electricity + 20 + 15) * 1.20
    total += electricity + 20 + 15 + (electricity + 20 + 15) * 1.20

average = total / months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {average:.2f} lv")





