number = float(input())

if number == 0:
    print("zero")
elif 0 < abs(number) < 1:
    if 0 < number < 1:
        print("small positive")
    elif -1 < number < 0:
        print("small negative")

elif 1 <= abs(number) <= 1000000:
    if 1 <= number <= 1000000:
        print("positive")
    elif -1 >= number >= -1000000:
        print("negative")

else:  # abs(number) > 1 000 000
    if number > 1000000:
        print("large positive")
    elif number < -1000000:
        print("large negative")
