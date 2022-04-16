max_goals = 0
best_player_max_goals = ""
player_scored_hattrick = False


while max_goals < 10:
    player = input()
    if player == "END":
        break
    else:
        goals = int(input())
        if goals > max_goals:
            max_goals = goals
            best_player_max_goals = player
        if max_goals >= 3:
            player_scored_hattrick = True
        if max_goals >= 10:
            break

print(f"{best_player_max_goals} is the best player!")
if player_scored_hattrick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")



