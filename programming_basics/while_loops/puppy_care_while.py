import sys
from sys import maxsize

total_food_kg = int(input())
total_food_grams = total_food_kg * 1000

total_eaten_food = 0
food_is_enough_till_adoption = True

command = input()

while total_food_grams >= -sys.maxsize:
    if command == "Adopted":
        break
    else:
        current_grams_eaten = int(command)
        total_food_grams -= current_grams_eaten
        total_eaten_food += current_grams_eaten
        if total_food_grams < 0:
            food_is_enough_till_adoption = False

        command = input()

diff = abs(total_food_kg * 1000 - total_eaten_food)
if food_is_enough_till_adoption:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
