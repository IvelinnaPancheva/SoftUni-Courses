num_of_cars = int(input())
cars = {}  # {car : {"mileage" : int mileage, "fuel": int fuel}, car: {.... } }

for _ in range(num_of_cars):
    data = input().split("|")
    # "{car}|{mileage}|{fuel}"
    car, mileage, fuel = data[0], int(data[1]), int(data[2])
    if car not in cars:
        cars[car] = {"mileage": mileage, "fuel": fuel}

command = input()

while command != "Stop":
    split_data = command.split(" : ")

    # "Drive : {car} : {distance} : {fuel}":
    if split_data[0] == "Drive":
        car, distance, fuel = split_data[1], int(split_data[2]), int(split_data[3])
        if car in cars:
            if cars[car]["fuel"] < fuel:
                print("Not enough fuel to make that ride")
            else: # fuel is enough
                cars[car]["mileage"] += distance
                cars[car]["fuel"] -= fuel
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                if cars[car]["mileage"] > 100000:
                    print(f"Time to sell the {car}!")
                    del cars[car]

    #"Refuel : {car} : {fuel}":
    elif split_data[0] == "Refuel":
        car, fuel = split_data[1], int(split_data[2])
        if car in cars:
            if cars[car]["fuel"] + fuel > 75:
                print(f"{car} refueled with {75 - cars[car]['fuel']} liters")
                cars[car]["fuel"] = 75
            else: # cars[car]["fuel"] + fuel <= 75 max
                cars[car]["fuel"] += fuel
                print(f"{car} refueled with {fuel} liters")

   # "Revert : {car} : {kilometers}":
    elif split_data[0] == "Revert":
        car, km_to_decrease = split_data[1], int(split_data[2])
        if car in cars and cars[car]["mileage"] >= km_to_decrease:
            cars[car]["mileage"] -= km_to_decrease
            if cars[car]["mileage"] < 10000:
                cars[car]["mileage"] = 10000
            else: # mileage > 10000
                print(f"{car} mileage decreased by {km_to_decrease} kilometers")

    command = input()

for car, data in cars.items():
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")
