num_of_cars = int(input())
cars = {}

for _ in range(num_of_cars):
    data = input().split("|")
    # "{car}|{mileage}|{fuel}"
    car, mileage, fuel = data[0], int(data[1]), int(data[2])
    if car not in cars:
        cars[car] = [mileage, fuel]

command = input()

while command != "Stop":
    split_data = command.split(" : ")

    # "Drive : {car} : {distance} : {fuel}":
    if split_data[0] == "Drive":
        car, distance, fuel = split_data[1], int(split_data[2]), int(split_data[3])
        if car in cars:
            if cars[car][1] < fuel:
                print("Not enough fuel to make that ride")
            else: # fuel is enough
                cars[car][0] += distance
                cars[car][1] -= fuel
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                if cars[car][0] > 100000:
                    print(f"Time to sell the {car}!")
                    del cars[car]

    #"Refuel : {car} : {fuel}":
    elif split_data[0] == "Refuel":
        car, fuel = split_data[1], int(split_data[2])
        if car in cars:
            if cars[car][1] + fuel > 75:
                print(f"{car} refueled with {75 - cars[car][1]} liters")
                cars[car][1] = 75
            else: # cars[car][1] + fuel <= 75 max
                cars[car][1] += fuel
                print(f"{car} refueled with {fuel} liters")

   # "Revert : {car} : {kilometers}":
    elif split_data[0] == "Revert":
        car, km_to_decrease = split_data[1], int(split_data[2])
        if car in cars and cars[car][0] >= km_to_decrease:
            cars[car][0] -= km_to_decrease
            if cars[car][0] < 10000:
                cars[car][0] = 10000
            else: # mileage > 10000
                print(f"{car} mileage decreased by {km_to_decrease} kilometers")

    command = input()

for car, data in cars.items():
    print(f"{car} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.")
