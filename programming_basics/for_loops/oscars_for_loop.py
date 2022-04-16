actor = input()
points = float(input())
reviewers = int(input()) # number of iterations unless points >= 1250.5

for reviewer_name in range(1, reviewers + 1):
    reviewer_name = input()
    reviewer_points = float(input())
    points += len(reviewer_name) * reviewer_points / 2
    if points > 1250.5:
        break

if points > 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {points:.1f}!")
else:
    diff = abs(points - 1250.5)
    print(f"Sorry, {actor} you need {diff:.1f} more!")

# •	Име на актьора - текст
# •	Точки от академията - реално число в интервала [2.0... 450.5]
# •	Брой оценяващи n - цяло число в интервала[1… 20]
# На следващите n-на брой реда:
# o	Име на оценяващия - текст
# o	Точки от оценяващия - реално число в интервала [1.0... 50.0]