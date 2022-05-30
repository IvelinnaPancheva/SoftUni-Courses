data = input().split(" ")
products = {}

while data[0] != "buy":
    product_name, price, quantity = data[0], float(data[1]), int(data[2])
    if product_name not in products:
        products[product_name] = [price, quantity]
    else:  # product name is an existing key
        if products[product_name][0] != price:
            products[product_name][0] = price
        products[product_name][1] += quantity

    data = input().split(" ")

for product in products:
    total_price = products[product][0] * products[product][1]
    print(f"{product} -> {total_price:.2f}")