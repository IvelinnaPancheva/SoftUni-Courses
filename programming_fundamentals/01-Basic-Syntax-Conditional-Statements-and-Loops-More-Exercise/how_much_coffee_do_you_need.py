command = input()

coffee_counter = 0

while coffee_counter < 6:
    if command == "END":
        break
    else: # command != "END"
        if command.isupper():
            if command == "CODING" or command == "CAT" or command == "DOG" or command == "MOVIE":
                coffee_counter += 2
            else:
                coffee_counter += 0
        if command.islower():
            if command == "coding" or command == "cat" or command == "dog" or command == "movie":
                coffee_counter += 1
            else:
                coffee_counter += 0
    command = input()

if coffee_counter >= 6:
    print("You need extra sleep")
else:
    print(coffee_counter)