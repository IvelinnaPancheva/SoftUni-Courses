data = input().split(" ")
searched_products = input().split(" ")
products = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index+1])
    products[key] = value

for product in searched_products:
    if product not in products.keys():
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {products[product]} of {product} left")

