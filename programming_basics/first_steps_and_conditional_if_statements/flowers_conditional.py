chrysanthemum = int(input())
roses = int(input())
tulips = int(input())
season = input()
is_holiday = input()

total = 0
if season == "Spring" or season == "Summer":
    if is_holiday == "Y":
        total = 1.15 * (chrysanthemum * 2 + roses * 4.10 + tulips * 2.50)
    else:
        total = chrysanthemum * 2 + roses * 4.10 + tulips * 2.50
    if season == "Spring" and tulips > 7:
        total = 0.95 * total

elif season == "Аutumn" or season == "Winter":
    if is_holiday == "Y":
        total = 1.15 * (chrysanthemum * 3.75 + roses * 4.50 + tulips * 4.15)
    else:
        total = chrysanthemum * 3.75 + roses * 4.50 + tulips * 4.15
    if season == "Winter" and roses >= 10:
        total = 0.90 * total

if (tulips + chrysanthemum + roses) > 20:
    total = 0.8 * total

total = total + 2

print(f"{total:.2f}")