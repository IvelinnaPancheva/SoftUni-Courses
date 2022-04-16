students = int(input())

average_grade = 0
excellent_counter = 0
good_counter = 0
bad_counter = 0
fail_counter = 0

for exams in range(1, students+1):
    grade = float(input())
    average_grade += grade
    if grade >= 5:
        excellent_counter += 1
    elif 4 <= grade <= 4.99:
        good_counter += 1
    elif 3 <= grade <= 3.99:
        bad_counter += 1
    else: # <3 fail
        fail_counter += 1

average_grade = average_grade / students
excellent_percent = excellent_counter / students * 100
good_percent = good_counter  / students * 100
bad_percent = bad_counter / students * 100
fail_percent = fail_counter / students * 100

print(f"Top students: {excellent_percent:.2f}%")
print(f"Between 4.00 and 4.99: {good_percent:.2f}%")
print(f"Between 3.00 and 3.99: {bad_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average_grade:.2f}")


# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# •	За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
# Изход
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
# Ред 1 -	"Top students: {процент студенти с успех 5.00 или повече}%"
# Ред 2 -	"Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
# Ред 3 -	"Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
# Ред 4 -	"Fail: {по-малко от 3.00}%"
# Ред 5 -	"Average: {среден успех}"
# Всички числа трябва да са форматирани до вторият знак след десетичната запетая.