data = input()

cities = {}
while data != "Sail":
    # Santo Domingo||240000||630
    split_data = data.split("||")
    city, current_population, current_gold = split_data[0], int(split_data[1]), int(split_data[2])
    if city not in cities:
        cities[city] = [current_population, current_gold]
    else: # city is an existing key
        cities[city][0] += current_population
        cities[city][1] += current_gold

    data = input()

data = input()
while data != "End":
    split_data = data.split("=>")
    if split_data[0] == "Plunder":
        # "Plunder=>{town}=>{people}=>{gold}"
        town, people, gold = split_data[1], int(split_data[2]), int(split_data[3])
        if town in cities:
            cities[town][0] -= people
            cities[town][1] -= gold
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            if cities[town][0] == 0 or cities[town][1] == 0:
                del cities[town]
                print(f"{town} has been wiped off the map!")

    elif split_data[0] == "Prosper":
        # "Prosper=>{town}=>{gold}"
        town, gold = split_data[1], int(split_data[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else: # gold not negative number
            if town in cities:
                cities[town][1] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

    data = input()

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town in cities.keys():
        print(f"{town} -> Population: {cities[town][0]} citizens, Gold: {cities[town][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")


