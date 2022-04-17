budget = float(input())
ticket_type = input()
fans = int(input())
tickets = 0

if 1 <= fans <= 4:
    budget = 0.25 * budget
elif 5 <= fans <= 9:
    budget = 0.40 * budget
elif 10 <= fans <= 24:
    budget = budget * 0.50
elif 25 <= fans <= 49:
    budget = 0.60 * budget
elif fans >= 50:
    budget = 0.75 * budget

if ticket_type == "VIP":
    tickets = fans * 499.99
    diff = abs(budget - tickets)
    if budget >= tickets:
        print(f"Yes! You have {diff:.2f} leva left.")
    else:
        print(f"Not enough money! You need {diff:.2f} leva.")
elif ticket_type == "Normal":
    tickets = fans * 249.99
    diff = abs(budget - tickets)
    if budget >= tickets:
        print(f"Yes! You have {diff:.2f} leva left.")
    else:
        print(f"Not enough money! You need {diff:.2f} leva.")


# •	VIP – 499.99 лева.
# •	Normal – 249.99 лева.
# Запалянковците имат определен бюджет, а броят на хората в групата определя какъв процент от бюджета трябва да се задели за транспорт:
# •	От 1 до 4 – 75% от бюджета.
# •	От 5 до 9 – 60% от бюджета.
# •	От 10 до 24 – 50% от бюджета.
# •	От 25 до 49 – 40% от бюджета.
# •	50 или повече – 25% от бюджета.