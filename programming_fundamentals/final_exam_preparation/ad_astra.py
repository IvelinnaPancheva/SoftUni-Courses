import re

text = input()

total_calories = 0
days = 0

food_info_pattern = r"(?P<separator>\||#)(?P<food>[a-zA-Z ]+)(\1)(?P<expiry>\d{2}\/\d{2}\/\d{2})(\1)(?P<calories>\d+)(\1)"

matches = re.finditer(food_info_pattern, text)

food_info = []
if matches:
    for match in matches:
        food = match.group("food")
        expiry = match.group("expiry")
        calories = int(match.group("calories"))

        total_calories += calories
        food_info.append(food)
        food_info.append(expiry)
        food_info.append(calories)

days = int(total_calories / 2000)

print(f"You have food to last you for: {days} days!")
for index in range(0, len(food_info), 3):
    print(f"Item: {food_info[index]}, Best before: {food_info[index+1]}, Nutrition: {food_info[index+2]}")
