
number_days = int(input())
total_food_grams = float(input())
days_counter = 0

cat_eats = 0
dog_eats = 0
total_eats = 0
biscuits = 0
total_biscuits = 0

for day in range(1, number_days + 1):
    dog_food_eaten = int(input())
    cat_food_eaten = int(input())
    cat_eats += cat_food_eaten
    dog_eats += dog_food_eaten
    days_counter += 1
    if days_counter % 3 == 0:
        biscuits = 0.1 * (cat_food_eaten + dog_food_eaten)
        total_biscuits += biscuits


total_eats = cat_eats + dog_eats
total_eats_percent = total_eats/ total_food_grams * 100
dog_eats = dog_eats / total_eats * 100
cat_eats = cat_eats / total_eats * 100

print(f"Total eaten biscuits: {total_biscuits:.0f}gr.")
print(f"{total_eats_percent:.2f}% of the food has been eaten.")
print(f"{dog_eats:.2f}% eaten from the dog.")
print(f"{cat_eats:.2f}% eaten from the cat.")






# На конзолата да се отпечатват четири реда:
# ⦁	"Total eaten biscuits: {количество изядени бисквитки}gr."
# ⦁	"{процент изядена храна}% of the food has been eaten."
# ⦁	"{процент изядена храна от кучето}% eaten from the dog."
# ⦁	"{процент изядена храна от котката}% eaten from the cat."
# Количеството изядени бисквитки трябва да бъде закръглено до най –
# близкото цяло число, а процентът храна трябва да бъде форматиран до втората цифра след десетичния знак.