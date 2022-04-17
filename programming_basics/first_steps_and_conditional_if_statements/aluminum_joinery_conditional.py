number_joinery = int(input())
type = str(input())
delivery = str(input())
price = 0

if number_joinery < 10:
    print("Invalid order")
elif number_joinery >= 10:
    if type == "90X130":
        if 30 < number_joinery <= 60:
            price = number_joinery * 110
            price -= price * 0.05
        elif number_joinery > 60:
            price = number_joinery * 110
            price -= price * 0.08
        elif 11 <= number_joinery <= 30:
            price = number_joinery * 110
    elif type == "100X150":
        if 40 < number_joinery <= 80:
            price = number_joinery * 140
            price -= price * 0.06
        elif number_joinery > 80:
            price = number_joinery * 140
            price -= price * 0.1
        elif 11 <= number_joinery <= 40:
            price = number_joinery * 140
    elif type == "130X180":
        if 20 < number_joinery <= 50:
            price = number_joinery * 190
            price -= price * 0.07
        elif number_joinery > 50:
            price = number_joinery * 190
            price -= price * 0.12
        elif 11 <= number_joinery <= 20:
            price = number_joinery * 190
    elif type == "200X300":
        if 25 < number_joinery <= 50:
            price = number_joinery * 250
            price -= price * 0.09
        elif number_joinery > 50:
            price = number_joinery * 250
            price -= price * 0.14
        elif 11 <= number_joinery <= 25:
            price = number_joinery * 250
    if delivery == "With delivery":
        price += 60

    if number_joinery > 99:
        price = price - 0.04 * price
    print(f"{price:.2f} BGN")