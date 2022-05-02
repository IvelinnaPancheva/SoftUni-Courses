n = int(input())

for x in range(1, n+1):
    x_as_string = str(x)
    sum_of_digits = 0
    for i in range(len(x_as_string)):
        j = int(x_as_string[i])
        sum_of_digits += j

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{x} -> True')
    else:
        print(f'{x} -> False')
