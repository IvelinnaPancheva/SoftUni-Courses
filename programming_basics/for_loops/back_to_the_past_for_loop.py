inherited_money = float(input())
last_year_of_carefree_life = int(input())

cost_of_living = 0
age = 17

for year in range(1800, (last_year_of_carefree_life + 1)):
    age += 1
    if year % 2 == 0:
        cost_of_living += 12000
    else:
        cost_of_living += 12000 + 50 * age

diff = abs(inherited_money - cost_of_living)

if inherited_money >= cost_of_living:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left." )
else:
    print(f"He will need {diff:.2f} dollars to survive." )




# Иванчо е на 18 години и получава наследство, което се състои от X сума пари и машина на времето.
# Той решава да се върне до 1800 година, но не знае дали парите ще са достатъчни,
# за да живее без да работи. Напишете програма, която пресмята,
# дали Иванчо ще има достатъчно пари, за да не се налага да работи до дадена година включително.
# Като приемем, че за всяка четна (1800, 1802 и т.н.) година ще харчи 12 000 лева.
# За всяка нечетна (1801,1803  и т.н.) ще харчи 12 000 + 50 * [годините, които е навършил през дадената година].
