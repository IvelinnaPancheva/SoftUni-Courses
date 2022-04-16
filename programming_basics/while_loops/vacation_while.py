vacation_cost = float(input())
budget = float(input())

days_counter = 0
spending_days_counter = 0



while budget < vacation_cost and spending_days_counter < 5:
    command = input()
    amount = float(input())
    if command == "spend":
        budget -= amount
        days_counter += 1
        spending_days_counter += 1
        if budget < 0:
            budget = 0
        if spending_days_counter == 5:
            break


    elif command == "save":
        days_counter += 1
        spending_days_counter = 0
        budget += amount

if budget >= vacation_cost:
    print(f"You saved the money for {days_counter} days.")
else:
    print(f"You can't save the money.")
    print(f"{days_counter}")

# От конзолата се четат:
# •	Пари, нужни за екскурзията - реално число;
# •	Налични пари - реално число.
# След това многократно се четат по два реда:
# •	Вид действие – текст с две възможности: "spend" или "save";
# •	Сумата, която ще спести/похарчи - реално число.