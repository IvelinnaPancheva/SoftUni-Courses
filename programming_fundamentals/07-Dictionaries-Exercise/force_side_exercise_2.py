command = input()

force_sides = dict()

while command != "Lumpawaroo":
    if " | " in command:
        side, user = command.split(" | ")
        user_does_not_exist = True
        for key, values in force_sides.items():
            if user in values:
                user_does_not_exist = False
                break
        if user_does_not_exist:
            if side not in force_sides:
                force_sides[side] = []
         # side is an existing key
            force_sides[side].append(user)

    elif " -> " in command:
        user, side = command.split(" -> ")
        for key, values in force_sides.items():
            if user in values:
                force_sides[key].remove(user)
                break
        if side not in force_sides:
            force_sides[side] = []
        force_sides[side].append(user)

        print(f"{user} joins the {side} side!")

    command = input()

for side in force_sides:
    if len(force_sides[side]) > 0:
        print(f"Side: {side}, Members: {len(force_sides[side])}")
        for player in force_sides[side]:
            print(f"! {player}")