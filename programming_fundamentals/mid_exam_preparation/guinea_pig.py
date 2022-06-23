food_kg = float(input())
hay_kg = float(input())
cover_kg = float(input())
weight_kg = float(input())

food_grams = food_kg * 1000
hay_grams = hay_kg * 1000
cover_grams = cover_kg * 1000
weight_grams = weight_kg * 1000

for i in range(1, 31):
    food_grams -= 300
    if food_grams <= 0:
        print("Merry must go to the pet store!")
        break
    if i % 2 == 0:
        hay_grams -= 0.05 * food_grams
        if hay_grams <= 0:
            print("Merry must go to the pet store!")
            break
    if i % 3 == 0:
        cover_grams -= weight_grams / 3
        if cover_grams <= 0:
            print("Merry must go to the pet store!")
            break

if food_grams > 0 and hay_grams > 0 and cover_grams > 0:
    print(f"Everything is fine! Puppy is happy! Food: {(food_grams / 1000):.2f}, Hay: {(hay_grams /1000):.2f},"
          f" Cover: {(cover_grams / 1000):.2f}.")