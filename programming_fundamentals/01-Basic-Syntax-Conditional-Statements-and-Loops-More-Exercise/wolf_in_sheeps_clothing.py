text = input()

list_variable = text.split(", ")
number = 0

for i in range(len(list_variable)-1, -1, -1):
    if list_variable[i] == "wolf" and i == len(list_variable) - 1:
        print("Please go away and stop eating my sheep")

    if list_variable[i] == "sheep":
        number += 1

    if list_variable[i] == "wolf"and i != len(list_variable) - 1:
        print(f"Oi! Sheep number {number}! You are about to be eaten by a wolf!")


