numbers_list = input().split(" ")

greater_5_than_average = []
for index in range(len(numbers_list)):
    numbers_list[index] = int(numbers_list[index])

average = sum(numbers_list) / len(numbers_list)

for index in range(len(numbers_list)):
    if numbers_list[index]  > average:
        greater_5_than_average.append(numbers_list[index])

if len(greater_5_than_average) == 0:
    print("No")
else:
    greater_5_than_average = sorted(greater_5_than_average, reverse=True)
    for index in range(len(greater_5_than_average)):
        greater_5_than_average[index] = str(greater_5_than_average[index])
    print(" ".join(greater_5_than_average[0:5]))

