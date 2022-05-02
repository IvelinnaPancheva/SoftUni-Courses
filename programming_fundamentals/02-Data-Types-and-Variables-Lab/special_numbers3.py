n = int(input())

for x in range(1, n+1):
    sum_of_digits = 0
    i = x
    while i > 0:
        sum_of_digits += i % 10
        i = int(i / 10)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{x} -> True')
    else:
        print(f'{x} -> False')
