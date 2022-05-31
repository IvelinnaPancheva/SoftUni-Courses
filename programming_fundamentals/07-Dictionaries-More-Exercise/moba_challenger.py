data = input()

players = {}

while data != "Season end":
    if " -> " in data:
        # "{player} -> {position} -> {skill}"
        split_data = data.split(" -> ")
        player, position, skill = split_data[0], split_data[1], int(split_data[2])

        if player not in players:
            players[player] = {position: skill}
        else: # player exists already with position + skill
            if position not in players[player].keys():
                players[player][position] = skill
            else: # position exists with skill, check current and dict value
                if skill > players[player][position]:
                    players[player][position] = skill

    else: # duel commmand
        # "{player} vs {player}"
        split_data = data.split(" vs ")
        first_player, second_player = split_data[0], split_data[1]
        if first_player in players and second_player in players:
            first_total_skill = 0
            second_total_skill = 0
            for first_position in players[first_player]:
                for second_position in players[second_player]:
                    if first_position == second_position:
                        first_total_skill += players[first_player][first_position]
                        second_total_skill += players[second_player][second_position]
            if first_total_skill > second_total_skill:
                del players[second_player]
            elif second_total_skill > first_total_skill:
                del players[first_player]
    data = input()

total_skills = {}
for player, positions in players.items():
    skills = 0
    for key, value in positions.items():
        skills += value
    total_skills[player] = skills

sorted_skills = sorted(total_skills.items(), key= lambda x: (-x[1], x[0]))

for pair in sorted_skills:
    print(f"{pair[0]}: {pair[1]} skill")
    for player in players.keys():
        if pair[0] == player:
            sub_dict = players[player]
            sub_dict = sorted(sub_dict.items(), key= lambda x: (-x[1], x[0]))
            for new_pair in sub_dict:
                print(f"- {new_pair[0]} <::> {new_pair[1]}")