n = int(input())
brackets_sum = ""
counter_open = 0
counter_closing = 0
balance_counter = 0

for i in range(n):
    entry = input()
    if entry == "(":
        counter_open += 1
        balance_counter += 1

    if entry == ")":
        counter_closing += 1
        if counter_open == counter_closing:
            balance_counter -= 1
        else:
            balance_counter += 1

if counter_open == counter_closing and balance_counter == 0:
    print("BALANCED")
else:
    print("UNBALANCED")