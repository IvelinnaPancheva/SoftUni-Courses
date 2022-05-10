numbers_as_string = input().split(", ")
numbers_as_integers = []


for num in numbers_as_string:
    numbers_as_integers.append(int(num))

for num in numbers_as_integers:
    if num == 0:
        numbers_as_integers.remove(num)
        numbers_as_integers.append(0)

print(numbers_as_integers)