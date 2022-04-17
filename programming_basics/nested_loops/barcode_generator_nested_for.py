beginning_number = input()  # 1111
ending_number = input()  # 9999

for number1 in range(int(beginning_number[0]), int(ending_number[0]) + 1):
    for number2 in range(int(beginning_number[1]), int(ending_number[1]) + 1):
        for number3 in range(int(beginning_number[2]), int(ending_number[2]) + 1):
            for number4 in range(int(beginning_number[3]), int(ending_number[3]) + 1):
                if number1 % 2 != 0 and number2 % 2 != 0 and number3 % 2 != 0 and number4 % 2 != 0:
                    print(f"{number1}{number2}{number3}{number4}", end = " ")


