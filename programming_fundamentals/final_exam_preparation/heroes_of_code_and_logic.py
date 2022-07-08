number_of_heroes = int(input())
heroes = {}
for _ in range(number_of_heroes):
    # "{hero name} {HP} {MP}"
    data = input().split(" ")
    hero, hit_points, mana_points = data[0], int(data[1]), int(data[2])
    if hero not in heroes:
        heroes[hero] = [hit_points, mana_points]

data = input()

while not data == "End":
    split_data = data.split(" - ")
    # "CastSpell – {hero name} – {MP needed} – {spell name}"
    if split_data[0] == "CastSpell":
        hero, mana_needed, spell = split_data[1], int(split_data[2]), split_data[3]
        if heroes[hero][1] >= mana_needed:
            heroes[hero][1] -= mana_needed
            print(f"{hero} has successfully cast {spell} and now has {heroes[hero][1]} MP!")

        else:
            print(f"{hero} does not have enough MP to cast {spell}!")

    # "TakeDamage – {hero name} – {damage} – {attacker}"
    elif split_data[0] == "TakeDamage":
        hero, damage, attacker = split_data[1], int(split_data[2]), split_data[3]
        heroes[hero][0] -= damage
        if heroes[hero][0] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!")
        else: # hit <= 0
            del heroes[hero]
            print(f"{hero} has been killed by {attacker}!")

    # "Recharge – {hero name} – {amount}"
    elif split_data[0] == "Recharge":
        hero, amount = split_data[1], int(split_data[2])
        if heroes[hero][1] + amount > 200:
            print(f"{hero} recharged for {200 - heroes[hero][1]} MP!")
            heroes[hero][1] = 200

        else: # heroes[hero][1] + amount <= 200
            print(f"{hero} recharged for {amount} MP!")
            heroes[hero][1] += amount

    # "Heal – {hero name} – {amount}"
    elif split_data[0] == "Heal":
        hero, amount = split_data[1], int(split_data[2])

        if heroes[hero][0] + amount > 100:
            print(f"{hero} healed for {100 - heroes[hero][0]} HP!")
            heroes[hero][0] = 100
        else:  # heroes[hero][0] + amount <= 100
            print(f"{hero} healed for {amount} HP!")
            heroes[hero][0] += amount

    data = input()

for hero in heroes:
    print(f"{hero}")
    print(f"  HP: {heroes[hero][0]}\n  MP: {heroes[hero][1]}")