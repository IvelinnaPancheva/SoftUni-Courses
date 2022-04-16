target_amount = int(input())

cash_payment_counter = 0
card_payment_counter = 0
sum_sales = 0
transaction_counter = 0

average_cash_payment = 0
average_card_payment = 0

while sum_sales < target_amount:
    command = input()
    if command != "End":
        current_transaction = int(command)
        transaction_counter += 1
        if transaction_counter % 2 != 0: # нечетна транзакция, в брой
            if current_transaction > 100:
                print(f"Error in transaction!")
            else:  #  транзакция <= 100 lv, successful cash payment
                cash_payment_counter += 1
                sum_sales += current_transaction
                average_cash_payment += current_transaction
                print(f"Product sold!")

        else:  # четна транзакция, only with credit card
            if current_transaction < 10:
                print(f"Error in transaction!")
            else: # current transacton > 10, card payment will be successful
                card_payment_counter += 1
                sum_sales += current_transaction
                average_card_payment += current_transaction
                print(f"Product sold!")

    if command == "End":
        print("Failed to collect required money for charity.")
        break


if sum_sales >= target_amount:
    average_card_payment = average_card_payment / card_payment_counter
    average_cash_payment = average_cash_payment / cash_payment_counter
    print(f"Average CS: {average_cash_payment:.2f}")
    print(f"Average CC: {average_card_payment:.2f}")

