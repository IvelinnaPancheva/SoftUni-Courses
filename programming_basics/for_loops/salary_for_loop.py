tabs = int(input())   # брой проверки в цикъла
salary = float(input())

fine = 0

for site in range(1, (tabs + 1)):
    site = input()
    if site == "Facebook":
        fine += 150
    if site == "Instagram":
        fine += 100
    if site == "Reddit":
        fine += 50

    if fine >= salary:
        break

if fine >= salary:
    print("You have lost your salary.")
else:
    diff = int(salary - fine)
    print(diff)


# •	"Facebook" -> 150 лв.
# •	"Instagram" -> 100 лв.
# •	"Reddit" -> 50 лв.
# От конзолата се четат два реда:
# •	Брой отворени табове в браузъра n - цяло число в интервала [1...10]
# •	Заплата - число в интервала [500...1500]