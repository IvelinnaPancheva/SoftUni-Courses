import re

command = input()

validation_pattern = r"%(?P<customer>[A-Z][a-z]+)%(?P<other>[^\|\$%\.]*)<(?P<product>\w+)>([^\|\$%\.]*)\|(?P<count>\d+)\|([^\|\$%\.0-9]*)(?P<price>\d+\.*\d*)\$"

total_price = 0
income = 0

while command != "end of shift":
    matches = re.finditer(validation_pattern, command)
    if matches:
        for match in matches:
            customer = match.group("customer")
            product = match.group("product")
            count = int(match.group("count"))
            price = float(match.group("price"))
            total_price = count * price
            print(f"{customer}: {product} - {total_price:.2f}")
            income += total_price

    command = input()

print(f"Total income: {income:.2f}")