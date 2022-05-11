product_type = input()
product_quantity = int(input())

if product_type == "coffee":
    order_price = product_quantity * 1.50
elif product_type == "water":
    order_price = product_quantity * 1
elif product_type == "coke":
    order_price = product_quantity * 1.4
elif product_type == "snacks":
    order_price = product_quantity * 2

print(f"{order_price:.2f}")