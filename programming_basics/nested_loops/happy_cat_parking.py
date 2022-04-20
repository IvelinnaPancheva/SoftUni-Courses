days = int(input())
hours_per_day = int(input())
total_paring = 0

for day in range(1, days + 1):
    parking_per_day = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking_per_day += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            parking_per_day += 1.25
        else:
            parking_per_day += 1
    total_paring += parking_per_day
    print(f"Day: {day} - {parking_per_day:.2f} leva")
print(f"Total: {total_paring:.2f} leva")