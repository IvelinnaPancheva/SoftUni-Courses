command = input()
products_in_stock = {}

while not command == "statistics":
    key, value = command.split(": ")
    if key not in products_in_stock:
        products_in_stock[key] = int(value)
    else:   # product is an existing key of the dict
        products_in_stock[key] += int(value)
    command = input()

print(f"Products in stock:")
[print(f"- {key}: {value}") for (key, value) in products_in_stock.items()]
print(f"Total Products: {len(products_in_stock)}")
print(f"Total Quantity: {sum(products_in_stock.values())}")