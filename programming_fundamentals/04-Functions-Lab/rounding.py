float_sequence = input().split(" ")

for index in range(len(float_sequence)):
    float_sequence[index] = round(float(float_sequence[index]))

print(float_sequence)