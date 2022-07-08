import re

pattern_barcode = r"@#+[A-Z][A-Za-z0-9]{4}[A-Za-z0-9]*[A-Z]@#+"

n = int(input())

for _ in range(n):
    barcode = input()

    match = re.findall(pattern_barcode, barcode)

    if match:
        valid_barcode = "".join(match)
        product_group = ""
        for char in valid_barcode:
            if char.isdigit():
                product_group += char

        if product_group == "":
            product_group = "00"

        print(f"Product group: {product_group}")

    else: # no match, empty list
        print("Invalid barcode")

