n = int(input())
even = list()
odd = []
negative = list()
positive = list()

for i in range(n):
    current_number = int(input())
    if current_number % 2 == 0:
        even.append(current_number)
    else:
        odd.append(current_number)
    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

keyword = input()
print(eval(keyword))