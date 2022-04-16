groups = int(input())

total_climbers = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for climbers in range (1, groups + 1):
    climbers = int(input())
    total_climbers += climbers
    if climbers <= 5:
        musala += climbers
    elif 6 <= climbers <= 12:
        monblan += climbers
    elif 13 <= climbers <= 25:
        kilimandjaro += climbers
    elif 26 <= climbers <= 40:
        k2 += climbers
    elif climbers >= 41:
        everest += climbers

musala_percent = musala / total_climbers * 100
monblan_percent = monblan / total_climbers * 100
kilimandjaro_percent = kilimandjaro / total_climbers * 100
k2_percent = k2 / total_climbers * 100
everest_percent = everest / total_climbers * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")