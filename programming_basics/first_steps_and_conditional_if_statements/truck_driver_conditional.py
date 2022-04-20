season = input()  # 1 season = 4 months
km_month = float(input())

salary = 0

if km_month <= 5000:
    if season == "Autumn" or season == "Spring":
        salary = 0.75 * km_month * 4
    elif season == "Summer":
        salary = 0.90 * km_month * 4
    elif season == "Winter":
        salary = 1.05 * km_month * 4
elif 5000 < km_month <= 10000:
    if season == "Autumn" or season == "Spring":
        salary = 0.95 * km_month * 4
    elif season == "Summer":
        salary = 1.10 * km_month * 4
    elif season == "Winter":
        salary = 1.25 * km_month * 4
elif 10000 < km_month <=20000:
    salary = 1.45 * km_month * 4

salary = 0.90 * salary # taxes

print(f"{salary:.2f}")

#                                   Пролет/Есен	    Лято	         Зима
# км на месец <= 5000	            0.75 лв./км	    0.90 лв./км	    1.05 лв./км
# 5000 < км на месец <= 10000	    0.95 лв./км	    1.10 лв./км	    1.25 лв./км
# 10000 < км на месец <= 20000	       1.45 лв./км – за който и да е сезон
#
# След като са извадени 10% за данъци се отпечатват останалите пари.
# Вход
# Входът се чете от конзолата и се състои от два реда:
# •	Първи ред – Сезон – текст "Spring", "Summer", "Autumn" или "Winter"
# •	Втори ред –  Километри на месец – реално число в интервала [10.00...20000.00]
