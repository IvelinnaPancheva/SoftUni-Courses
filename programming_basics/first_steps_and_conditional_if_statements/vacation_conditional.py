budget = float(input())
season = input()  # текст "Summer" или "Winter"

accommodation = ""
location = ""

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        budget = 0.65 * budget
    elif season == "Winter":
        location = "Morocco"
        budget = 0.45 * budget
elif 100 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        budget = 0.80 * budget
    elif season == "Winter":
        location = "Morocco"
        budget = 0.60 * budget
else: # budget > 3000
    accommodation = "Hotel"
    budget = 0.90 * budget
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {accommodation} - {budget:.2f}")

# •	При бюджет по-малък или равен от 1000лв.:
# o	Настаняване в "Camp"
# o	Според сезона локацията ще е една от следните и ще струва определен процент от бюджета:
# 	Лято – Аляска – 65% от бюджета
# 	Зима – Мароко – 45% от бюджета
# •	При бюджет по-голям от 1000лв. и по-малък или равен от 3000лв.:
# o	Настаняване в "Hut"
# o	Според сезона локацията ще е една от следните и ще струва определен процент от бюджета:
# 	Лято – Аляска – 80% от бюджета
# 	Зима – Мароко – 60% от бюджета
# •	При бюджет по-голям от 3000лв.:
# o	Настаняване в "Hotel"
# o	Според сезона локацията ще е една от следните и ще струва 90% от бюджета:
# 	Лято – Аляска
# 	Зима – Мароко
# отпечатат един ред.
# "{локацията} – {мястото за настаняване} – {цената}"
# Цената трябва да е форматирана до вторият знак след десетичната запетая.