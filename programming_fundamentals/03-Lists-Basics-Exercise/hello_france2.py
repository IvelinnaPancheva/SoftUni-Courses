items_and_prices = input()
budget = float(input())

items_price_list = items_and_prices.split("|")
new_price_list = list()
sales_income = 0

for item in items_price_list:
    if budget <= 0:
        break
    item_type = item.split("->")[0]
    item_price = float(item.split("->")[1])

    if "Clothes" in item_type:
        if item_price <= 50 and item_price <= budget:
            budget -= item_price
            new_price = item_price * 1.4
            new_price_list.append(new_price)
            sales_income += new_price

    if "Shoes" in item_type:
        if item_price <= 35 and item_price <= budget:
            budget -= item_price
            new_price = item_price * 1.4
            new_price_list.append(new_price)
            sales_income += new_price

    if "Accessories" in item_type:
        if item_price <= 20.5 and item_price <= budget:
            budget -= item_price
            new_price = item_price * 1.4
            new_price_list.append(new_price)
            sales_income += new_price

profit = sum(new_price_list) - sum(new_price_list)/1.4
total_income = budget + sum(new_price_list)

for element in new_price_list:
    print(f"{element:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if total_income >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")