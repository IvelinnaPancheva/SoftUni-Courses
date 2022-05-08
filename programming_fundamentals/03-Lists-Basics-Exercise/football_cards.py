card_sequence = input()
card_list = card_sequence.split()
a_team = 11
b_team = 11
a_team_set = set()
b_team_set = set()
is_game_terminated = False

for i in range(len(card_list)):
    if "A" in card_list[i]:
        a_team_set.add(card_list[i])
        if a_team - len(a_team_set) < 7:
            is_game_terminated = True
            break

    elif "B" in card_list[i]:
        b_team_set.add(card_list[i])
        if b_team - len(b_team_set) < 7:
            is_game_terminated = True
            break

a_team = a_team - len(a_team_set)
b_team = b_team - len(b_team_set)

if is_game_terminated:
    print(f"Team A - {a_team}; Team B - {b_team}")
    print("Game was terminated")
else:
    print(f"Team A - {a_team}; Team B - {b_team}")