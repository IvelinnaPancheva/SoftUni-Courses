float_numbers_list = input().split(" ")

for i in range(len(float_numbers_list)):
    float_numbers_list[i] = abs(float(float_numbers_list[i]))

print(float_numbers_list)

