n = int(input())

for x in range(1, n+1):
    x_as_string = str(x)
    list_variable = list(x_as_string)
    sum_of_digits = 0
    for i in range(len(list_variable)):
        sum_of_digits += int(list_variable[i])

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{x} -> True')
    else:
        print(f'{x} -> False')
