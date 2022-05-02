coffee_counter = 0

while coffee_counter < 6:
    command = input()
    if command == "END":
        break
    else: # command != "END"
        if command.isupper():
            if command == "CODING" or command == "CAT" or command == "DOG" or command == "MOVIE":
                coffee_counter += 2
            else:
                continue
        if command.islower():
            if command == "coding" or command == "cat" or command == "dog" or command == "movie":
                coffee_counter += 1
            else:
                continue

if coffee_counter >= 6:
    print("You need extra sleep")
else:
    print(coffee_counter)