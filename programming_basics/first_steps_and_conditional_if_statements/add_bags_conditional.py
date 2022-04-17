price_20_kg = float(input())
bag_kg = float(input())
days_until_departure = int(input())
number_bags = int(input())

price_mimi = 0

if bag_kg < 10:
    price_mimi = price_20_kg * 0.2
elif 10 <= bag_kg <= 20:
    price_mimi = 0.5 * price_20_kg
else:
    price_mimi = price_20_kg

if days_until_departure > 30:
    price_mimi += 0.1 * price_mimi
elif 7 <= days_until_departure <= 30:
    price_mimi += 0.15 * price_mimi
else:
    price_mimi += 0.4 * price_mimi

total = price_mimi * number_bags
print(f" The total price of bags is: {total:.2f} lv. ")