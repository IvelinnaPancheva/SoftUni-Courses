def calculate_total_price(product, quantity):
    if product == "coffee":
        total_price = product_quantity * 1.50
    elif product == "water":
        total_price = product_quantity * 1
    elif product == "coke":
        total_price = product_quantity * 1.4
    elif product == "snacks":
        total_price = product_quantity * 2
    return total_price


product_type = input()
product_quantity = int(input())

print(f"{calculate_total_price(product_type, product_quantity):.2f}")