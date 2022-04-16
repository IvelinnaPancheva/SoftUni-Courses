number_games = int(input())  # number of iterations, inputs in the loop, number of points inputs

result = 0
counter_1 = 0
counter_2  = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
invalid_input_counter = 0

for game in range(1, number_games + 1):
    points = int(input())
    if points < 0 or points > 50:
        result /= 2
        invalid_input_counter += 1
    else:  # points > 0 and < 50
        if 0 <= points <= 9:
            result += 0.2 * points
            counter_1 += 1
        elif 10 <= points <= 19:
            result += 0.3 * points
            counter_2 += 1
        elif 20 <= points <= 29:
            result += 0.4 * points
            counter_3 += 1
        elif 30 <= points <= 39:
            result += 50
            counter_4 += 1
        elif 40 <= points <= 50:
            result += 100
            counter_5 += 1



print(f"{result:.2f}")
print(f"From 0 to 9: {(counter_1 / number_games * 100):.2f}%")
print(f"From 10 to 19: {(counter_2 / number_games * 100):.2f}%")
print(f"From 20 to 29: {(counter_3 / number_games * 100):.2f}%")
print(f"From 30 to 39: {(counter_4 / number_games * 100):.2f}%")
print(f"From 40 to 50: {(counter_5 / number_games * 100):.2f}%")
print(f"Invalid numbers: {(invalid_input_counter / number_games * 100):.2f}%")

# Изход
# Да се отпечата на конзолата 7 реда:
# •	1ви ред: "{Краен резултат}"
# •	2ри ред: "From 0 to 9: {процент в интервала}%"
# •	3ти ред: "From 10 to 19: {процент в интервала}%"
# •	4ти ред: "From 20 to 29: {процент в интервала}%"
# •	5ти ред: "From 30 to 39: {процент в интервала}%"
# •	6ти ред: "From 40 to 50: {процент в интервала}%"
# •	7ми ред: "Invalid numbers: {процент в интервала}%"
# Всички числа трябва да са форматирана до вторият знак след запетаята.


# •	От 0 до 9  20 % от числото
# •	От 10 до 19  30 % от числото
# •	От 20 до 29  40 % от числото
# •	От 30 до 39  50 точки
# •	От 40 до 50  100 точки
# •	Невалидно число  резултата се дели на 2
#
# Освен резултата програмата трябва да изкарва статистика за проценти числа в дадените интервали.
# Вход

