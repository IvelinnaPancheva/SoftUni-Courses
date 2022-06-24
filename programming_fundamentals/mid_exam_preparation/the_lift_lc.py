people = int(input())
lift_wagons_state = input().split(" ")
final_lift_wagons_state = []

lift_wagons_state = [int(x) for x in lift_wagons_state]
total_free_seats = len(lift_wagons_state) * 4 - sum(lift_wagons_state)

for i in range(len(lift_wagons_state)):
    current_free_seats = 4 - lift_wagons_state[i]
    if people >= current_free_seats:
        total_free_seats -= current_free_seats
        people -= current_free_seats
        final_lift_wagons_state.append(current_free_seats + lift_wagons_state[i])
    elif 0 < people <= current_free_seats:
        total_free_seats -= people
        final_lift_wagons_state.append(people+lift_wagons_state[i])
        people -= people
    elif people == 0:
        final_lift_wagons_state.append(lift_wagons_state[i])


final_lift_wagons_state = [str(x) for x in final_lift_wagons_state]
final_lift_wagons_state = " ".join(final_lift_wagons_state)

if people == 0 and total_free_seats > 0:
    print("The lift has empty spots!")
    print(final_lift_wagons_state)
elif total_free_seats == 0 and people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(final_lift_wagons_state)
elif people == 0 and total_free_seats == 0:
    print(final_lift_wagons_state)
