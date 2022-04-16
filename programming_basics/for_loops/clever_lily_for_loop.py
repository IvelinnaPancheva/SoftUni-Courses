age = int(input())  # no of iterations
washing_machine = float(input())
toy_price = int(input())

count_toys = 0
total = 0
birthday_money = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        birthday_money += 10
        total += birthday_money - 1
    else:
        count_toys += 1

total += count_toys * toy_price
diff = abs(total - washing_machine)

if total >= washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")


