from math import floor
group = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):
    coins += 50
    condition_3th_day = False
    if day % 10 == 0:
        group -= 2
    if day % 15 == 0:
        group += 5

    coins -= group * 2

    if day % 3 == 0:
        coins -= 3 * group
        condition_3th_day = True

    if day % 5 == 0:
        coins += 20 * group
        if condition_3th_day:
            coins -= group * 2
coins = floor(coins / group)
print(f"{group} companions received {coins} coins each.")

