player = input()

total_points = 301
success_counter = 0
fail_counter = 0

command = input()
while command != "Retire":
    current_points = int(input())
    if command == "Single":
        if total_points >= current_points:
            total_points -= current_points
            success_counter += 1
        else:
            fail_counter += 1
    elif command == "Double":
        current_points *= 2
        if total_points >= current_points:
            total_points -= current_points
            success_counter += 1
        else:
            fail_counter += 1
    elif command == "Triple":
        current_points *= 3
        if total_points >= current_points:
            total_points -= current_points
            success_counter += 1
        else:
            fail_counter += 1
    if total_points == 0:
        print(f"{player} won the leg with {success_counter} shots.")
        break
    command = input()
if command == "Retire":
    print(f"{player} retired after {fail_counter} unsuccessful shots.")



