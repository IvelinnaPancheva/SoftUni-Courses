import re

pattern = r">>(?P<product>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"

text = input()
furniture = []
total_sum = 0

while text != "Purchase":
    matches = re.finditer(pattern, text)
    if matches:
        for match in matches:
            product = match.group("product")
            price = float(match.group("price"))
            quantity = int(match.group("quantity"))
            furniture.append(product)
            total_sum += price * quantity

    text = input()

print("Bought furniture:")
[print(element) for element in furniture]
print(f"Total money spend: {total_sum:.2f}")