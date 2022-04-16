destination = input()

while destination != "End":
    min_budget = float(input())
    savings =  0
    if destination == "End":
        break
    while min_budget > savings:
        current_earnings = float(input())
        savings += current_earnings
        if savings >= min_budget:
            print(f"Going to {destination}!")

    destination = input()