working_day_events = input().split('|')

energy = 100
coins = 100
is_day_completed = False
success_counter = 0
orders = 0

for event in working_day_events:
    current_event = event.split("-")[0]
    current_value = int(event.split("-")[1])
    if current_event == "rest":
        if energy + current_value <= 100:
            energy += current_value
            print(f"You gained {current_value} energy.")
            print(f"Current energy: {energy}.")
        else:
            print(f"You gained {0} energy.")
            print(f"Current energy: {energy}.")
    elif current_event == "order":
        orders += 1
        if energy >= 30:
            energy -= 30
            coins += current_value
            print(f"You earned {current_value} coins.")
            success_counter += 1
        else: # energy < 30
            energy += 50
            print("You had to rest!")
    else:   # current_event == "ingredient"
        if coins >= current_value:
            coins -= current_value
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            is_day_completed = False
            break
    if success_counter == orders:
        is_day_completed = True

if is_day_completed:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


