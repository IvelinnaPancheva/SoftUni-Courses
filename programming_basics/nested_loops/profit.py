one_lev_coins = int(input())
two_lev_coins = int(input())
five_lev_notes = int(input())
amount = int(input())

for x in range(0, one_lev_coins + 1):
    for y in range(0, two_lev_coins + 1):
        for z in range(0, five_lev_notes + 1):
            if x * 1 + y * 2 + z * 5 == amount:
                print(f"{x} * 1 lv. + {y} * 2 lv. + {z} * 5 lv. = {amount} lv.")