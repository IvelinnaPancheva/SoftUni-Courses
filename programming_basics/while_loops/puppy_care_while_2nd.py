total_food_kg = int(input())
total_food_grams = total_food_kg * 1000

total_eaten_food = 0
food_is_enough_till_adoption = True

command = input()

while command != "Adopted":
    current_eaten_grams = int(command)
    total_eaten_food += current_eaten_grams
    if total_food_grams - total_eaten_food < 0:
        food_is_enough_till_adoption = False
    command = input()
    if command == "Adopted":

        break
diff = abs(total_food_grams - total_eaten_food)
if food_is_enough_till_adoption:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")


