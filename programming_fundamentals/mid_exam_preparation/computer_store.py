command = input()

total_price = 0
taxes = 0

while command != "special" and command != "regular":
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
    else:
        total_price += current_price
        taxes += 0.20 * current_price

    command = input()

receipt_price = total_price + taxes
if command == "special":
    receipt_price -= 0.1 * receipt_price
if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {receipt_price:.2f}$")
