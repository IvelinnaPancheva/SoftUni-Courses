square_meters = float(input())
price_before_discount = square_meters * 7.61
discount = price_before_discount * 0.18
final_price = price_before_discount - discount
print(f'The final price is {final_price} lv.')
print(f'The discount is {discount} lv.')