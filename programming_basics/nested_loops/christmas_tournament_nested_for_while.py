number_days = int(input())

wins_per_day_counter = 0
losses_per_day_counter = 0
total_wins = 0
total_losses = 0
daily_sum = 0
total_sum = 0

for day in range(1, number_days + 1):
    command = input()
    while command != "Finish":
        current_score = input()
        if current_score == "win":
            wins_per_day_counter += 1
            daily_sum += 20
        elif current_score == "lose":
            losses_per_day_counter += 1
        command = input()

    if command == "Finish":
        if wins_per_day_counter > losses_per_day_counter:
            total_wins += 1
            daily_sum = daily_sum * 1.1
            total_sum += daily_sum

        else: #losses_per_day_counter >= wins_per_day_counter:
            total_losses += 1
            total_sum += daily_sum

        daily_sum = 0
        wins_per_day_counter = 0
        losses_per_day_counter = 0

if total_wins > total_losses:
    total_sum = total_sum * 1.2
    print(f"You won the tournament! Total raised money: {total_sum:.2f}")
else: # elif total losses >= total wins
    print(f"You lost the tournament! Total raised money: {total_sum:.2f}")
