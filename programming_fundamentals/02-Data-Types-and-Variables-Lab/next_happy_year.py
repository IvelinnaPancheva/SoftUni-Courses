year = int(input())

year_as_string = str(year)
digits_set = set()
is_happy_year = False

for i in range(len(year_as_string)):
    digits_set.add(year_as_string[i])
    year += 1
    while not is_happy_year:
        year += 1
        if len(year_as_string) == len(digits_set):
            is_happy_year = True

if is_happy_year:
    print(year_as_string)
