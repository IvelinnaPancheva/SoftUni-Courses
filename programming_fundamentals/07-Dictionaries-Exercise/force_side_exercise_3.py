def add_user(forces_dict, user_to_be_added, side_to_check):
    user_does_not_exist = True
    for key, values in forces_dict.items():
        if user_to_be_added in values:
            user_does_not_exist = False
            break
    if user_does_not_exist:
        if side_to_check not in forces_dict:
            forces_dict[side_to_check] = []
        # side is an existing key
        forces_dict[side_to_check].append(user_to_be_added)
    return forces_dict


def change_user_side(forces_dict, user_to_be_changed, side_to_check):
    for key, values in forces_dict.items():
        if user_to_be_changed in values:
            forces_dict[key].remove(user_to_be_changed)
            break
    if side_to_check not in forces_dict:
        forces_dict[side_to_check] = []
    forces_dict[side_to_check].append(user_to_be_changed)
    return forces_dict


command = input()

force_sides = dict()

while command != "Lumpawaroo":
    if " | " in command:
        side, user = command.split(" | ")
        force_sides = add_user(force_sides, user, side)

    elif " -> " in command:
        user, side = command.split(" -> ")
        force_sides = change_user_side(force_sides, user,side)

        print(f"{user} joins the {side} side!")

    command = input()

for side in force_sides:
    if len(force_sides[side]) > 0:
        print(f"Side: {side}, Members: {len(force_sides[side])}")
        for player in force_sides[side]:
            print(f"! {player}")