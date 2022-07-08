n_of_plants = int(input())
plants_rarity = {}
for _ in range(n_of_plants):
    # "{plant}<->{rarity}"
    data = input().split("<->")
    plant = data[0]
    rarity = int(data[1])
    plants_rarity[plant] = rarity

plants_rating = {}
for plant in plants_rarity:
    plants_rating[plant] = []

data = input()
while data != "Exhibition":
    data = data.replace(" - ", ": ")
    split_data = data.split(": ")
    # "Rate: {plant} - {rating}"
    if split_data[0] == "Rate":
        plant, rating = split_data[1], int(split_data[2])
        if plant not in plants_rating:
            print("error")
        else: # plant is an existing key
            plants_rating[plant].append(rating)

    # "Update: {plant} - {new_rarity}"
    elif split_data[0] == "Update":
        plant, new_rarity = split_data[1], split_data[2]
        if plant not in plants_rarity:
            print("error")
        else: # plant is an existing key
            plants_rarity[plant] = new_rarity

    # "Reset: {plant}"
    elif split_data[0] == "Reset":
        plant = split_data[1]
        if plant not in plants_rating:
            print("error")
        else:  # plant is an existing key
            plants_rating[plant] = []

    data = input()

print("Plants for the exhibition:")
for plant, rarity in plants_rarity.items():
    for key, rating in plants_rating.items():
        if plant == key:
            if len(rating) != 0:
                average_rating = sum(rating) / len(rating)
                print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")
            else:
                print(f"- {plant}; Rarity: {rarity}; Rating: 0.00")
