def calculate_total_price(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1
    elif product == "coke":
        price = 1.4
    elif product == "snacks":
        price = 2
    return price * quantity


product_type = input()
product_quantity = int(input())

print(f"{calculate_total_price(product_type, product_quantity):.2f}")