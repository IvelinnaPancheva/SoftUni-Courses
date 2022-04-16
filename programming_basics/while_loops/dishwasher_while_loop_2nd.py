bottles_detergent = int(input())

ml_detergent = bottles_detergent * 750
dishes_counter = 0
pots_counter = 0
washing_counter = 0
detergent_was_enough = True

command = input()

while command != "End":
    current_dishes = int(command)
    washing_counter += 1
    if washing_counter % 3 == 0: # всяко трето зареждане с тенджери
        pots_counter += current_dishes
        ml_detergent -= current_dishes * 15
    else: # всяко зареждане без трето, само чинии
        dishes_counter += current_dishes
        ml_detergent -= current_dishes * 5
    if ml_detergent < 0:
        detergent_was_enough = False
        break
    command = input()

if detergent_was_enough:
    print(f"Detergent was enough!")
    print(f"{dishes_counter} dishes and {pots_counter} pots were washed.")
    print(f"Leftover detergent {ml_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(ml_detergent)} ml. more necessary!")

