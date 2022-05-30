data = input().split(" ")
products = {}   # {product_name: {"price" : float price, "quantity": int q}, product_name....

while data[0] != "buy":
    product_name, price, quantity = data[0], float(data[1]), int(data[2])
    if product_name not in products:
        products[product_name] = {"price": price, "quantity": quantity}
    else:  # product name is an existing key
        if products[product_name]["price"] != price:
            products[product_name]["price"] = price
            products[product_name]["quantity"] += quantity

    data = input().split(" ")

for product in products:
    total_price = products[product]["price"] * products[product]["quantity"]
    print(f"{product} -> {total_price:.2f}")