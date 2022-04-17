from math import floor
balls_number = int(input())

red_points = 0
orange_points = 0
yellow_points = 0
white_points = 0
black_divides = 0
total_points = 0
others_counter = 0

for ball in range(1, balls_number + 1):
    color = input()
    if color == "red":
        red_points += 1
        total_points += 5
    elif color == "orange":
        orange_points += 1
        total_points += 10
    elif color == "yellow":
        yellow_points += 1
        total_points += 15
    elif color == "white":
        white_points += 1
        total_points += 20
    elif color == "black":
        black_divides += 1
        total_points = floor(total_points / 2)
    else:
        others_counter += 1
        continue

print(f"Total points: {total_points}")
print(f"Points from red balls: {red_points}")
print(f"Points from orange balls: {orange_points}")
print(f"Points from yellow balls: {yellow_points}")
print(f"Points from white balls: {white_points}")
print(f"Other colors picked: {others_counter}")
print(f"Divides from black balls: {black_divides}")


