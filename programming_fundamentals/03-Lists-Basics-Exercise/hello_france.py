items_and_prices = input()
budget = float(input())

items_price_list = items_and_prices.split("|")
price_list = list()
new_price_list = list()
sales_income = 0
expenses = 0

for sub in items_price_list:
    current = float(sub.split("->")[1])
    price_list.append(current)

for i in range(len(items_price_list)):
    if budget <= 0:
        break
    if "Clothes" in items_price_list[i]:
        if price_list[i] <= 50 and price_list[i] <= budget:
            current_price = price_list[i]
            budget -= current_price
            expenses += current_price
            new_price = current_price * 1.4
            new_price_list.append(new_price)
            sales_income += new_price

    if "Shoes" in items_price_list[i]:
        if price_list[i] <= 35 and price_list[i] <= budget:
            current_price = price_list[i]
            budget -= current_price
            expenses += current_price
            new_price = current_price * 1.4
            new_price_list.append(new_price)
            sales_income += new_price

    if "Accessories" in items_price_list[i]:
        if price_list[i] <= 20.5 and price_list[i] <= budget:
            current_price = price_list[i]
            budget -= current_price
            expenses += current_price
            new_price = current_price * 1.4
            new_price_list.append(new_price)
            sales_income += new_price

profit = sales_income - expenses
total_income = budget + sales_income

for element in new_price_list:
    print(f"{element:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if total_income >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")