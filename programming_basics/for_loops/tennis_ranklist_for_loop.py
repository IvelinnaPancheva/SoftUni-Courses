from math import  floor

tournaments = int(input())
start_points = int(input())

points = 0
count_win = 0

for phase in range(tournaments):
    phase = input()
    if phase == "W":
        count_win += 1
        points += 2000
    elif phase == "F":
        points += 1200
    elif phase == "SF":
        points += 720

total_points = points + start_points
average_points = floor(points / tournaments)
win_percent = count_win / tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{win_percent:.2f}%")



# •	"Final points: {брой точки след изиграните турнири}"
# •	"Average points: {средно колко точки печели за турнир}"
# •	"{процент спечелени турнири}%"