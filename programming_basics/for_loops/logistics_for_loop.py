freight = int(input())   # number of for loop iterations

average_price_ton = 0
van_freights = 0
truck_freights = 0
train_freights = 0
total_price = 0
total_weight = 0

for transport in range(1, freight + 1):
    weight = int(input())
    total_weight += weight
    if weight <= 3:
        van_freights += weight
        total_price += 200 * weight
    elif 4 <= weight <= 11:
        truck_freights += weight
        total_price += 175 * weight
    elif weight >= 12:
        train_freights += weight
        total_price += 120 * weight

average_price_ton = total_price / total_weight
percent_van = van_freights / total_weight * 100
percent_truck = truck_freights / total_weight * 100
percent_train = train_freights/ total_weight * 100

print(f"{average_price_ton:.2f}")
print(f"{percent_van:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")

#  •	До 3 тона – микробус (200 лева на тон)
# •	От 4 до 11 тона – камион (175 лева на тон)
# •	12 и повече тона – влак (120 лева на тон)
# Вашата задача е да изчислите средната цена на тон превозен товар, както и процента на тоновете  превозвани
# с всяко превозно средство, спрямо общото тегло(в тонове) на всички товари.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на товарите за превоз – цяло число в интервала [1...1000]
# •	За всеки един товар на отделен ред – тонажа на товара – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 4 реда, както следва:
# •	Първи ред – средната цена на тон превозен товар (закръглена до втория знак след дес. запетая);
# •	Втори ред – процентът тона превозвани с микробус (процент между 0.00% и 100.00%);
# •	Трети ред – процентът  тона превозвани с камион (процент между 0.00% и 100.00%);
# •	Четвърти ред – процентът тона превозвани с влак (процент между 0.00% и 100.00%).