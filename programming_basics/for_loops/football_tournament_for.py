football_team = input()

wins_total = 0
draws_total = 0
losses_total = 0
points_total = 0
win_rate =0

number_games = int(input())
for game in range(number_games):
    score = input()
    if score == "W":
        wins_total += 1
        points_total += 3
    elif score == "D":
        draws_total += 1
        points_total += 1
    elif score == "L":
        losses_total += 1

if number_games == 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    win_rate = wins_total / number_games * 100
    print(f"{football_team} has won {points_total} points during this season.")
    print(f"Total stats:")
    print(f"## W: {wins_total}")
    print(f"## D: {draws_total}")
    print(f"## L: {losses_total}")
    print(f"Win rate: {win_rate:.2f}%")

