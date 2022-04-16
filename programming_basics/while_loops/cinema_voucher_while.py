voucher_amount = int(input())

movie_tickets_counter = 0
ticket_price = 0
other_purchase_counter = 0
purchase_price = 0

command = input()
while command != "End":
    if len(command) > 8: # movie ticket
        ticket_price = ord(command[0]) + ord(command[1])
        if voucher_amount >= ticket_price:
            movie_tickets_counter += 1
            voucher_amount -= ticket_price
        else: # voucher amount < ticket price
            break
    else: # len(command) <= 8 # other purchase
        purchase_price = ord(command[0])
        if voucher_amount >= purchase_price:
            other_purchase_counter += 1
            voucher_amount -= purchase_price
        else: # voucher amount < purchase price
            break
    command = input()

print(movie_tickets_counter)
print(other_purchase_counter)




# Ако името на покупката съдържа повече от 8 символа, то тя е билет за филм,
# а нейната цена представлява сумата на ASCII символите от първите ѝ два символа.
# Ако името на покупката съдържа 8 или по-малко символа,
# нейната цена е равна на стойността на първия ASCII символ в името.
# Любо въвежда името на покупките, които желае, докато не въведе "End"
# или не въведе покупка, чиято стойност е по-голяма от останалата сума на ваучера.
# След това до получаване на команда "End" или до изчерпването на ваучера, се чете по един ред:
# Покупката, която Любо е избрал – текст