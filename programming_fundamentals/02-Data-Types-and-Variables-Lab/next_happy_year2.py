year = int(input())

is_happy_year = False

while not is_happy_year:
    year += 1
    year_as_string = str(year)
    digits_set = set()

    for i in range(len(year_as_string)):
        digits_set.add(year_as_string[i])
        if len(year_as_string) == len(digits_set):
            is_happy_year = True
            break

if is_happy_year:
    print(year)
