num_of_dragons = int(input())

types = {}
damage_average = {}
health_average = {}
armor_average = {}

for _ in range(num_of_dragons):
    data = input().split(" ")
    # "{type} {name} {damage} {health} {armor}"
    type_dragon, name, damage, health, armor = data[0], data[1], data[2], data[3], data[4]

    if damage == "null":
        damage = 45
    else:
        damage = int(damage)


    if health == "null":
        health = 250
    else:
        health = int(health)

    if armor == "null":
        armor = 10
    else:
        armor = int(armor)

    stats = [damage, health, armor]

    if type_dragon not in types:
        types[type_dragon] = {name : stats}
        damage_average[type_dragon] = []
        health_average[type_dragon] = []
        armor_average[type_dragon] = []
    else:
        types[type_dragon][name] = stats


for dragontype, dragon_dict in types.items():
    for name in dragon_dict:
        for x in damage_average:
            if dragontype == x:
                damage_average[dragontype].append((types[dragontype][name])[0])
        for y in health_average:
            if dragontype == y:
                health_average[dragontype].append((types[dragontype][name])[1])
        for z in armor_average:
            if dragontype == z:
                armor_average[dragontype].append((types[dragontype][name])[2])


for type in damage_average.keys():
    damage_average[type] = sum(damage_average[type]) / len(damage_average[type])

for type in health_average:
    health_average[type] = sum(health_average[type]) / len(health_average[type])

for type in armor_average:
    armor_average[type] = sum(armor_average[type]) / len(armor_average[type])

for type in types:
    for x in damage_average:
        for y in health_average:
            for z in armor_average:
                if type == x == y == z:
                    print(f"{type}::({damage_average[x]:.2f}/{health_average[y]:.2f}/{armor_average[z]:.2f})")

    subdict = types[type]
    subdict = dict(sorted(subdict.items(), key=lambda x: x[0]))
    for dragon, stats_list in subdict.items():
        print(f"-{dragon} -> damage: {stats_list[0]}, health: {stats_list[1]}, armor: {stats_list[2]}")



