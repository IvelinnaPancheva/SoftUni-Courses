time_sequence = input().split(" ")
time_integers = []
sum_times1 = 0
sum_times2 = 0

for i in range(int(len(time_sequence) / 2)):
    current = int(time_sequence[i])
    sum_times1 += current
    if current == 0:
        sum_times1 = 0.8 * sum_times1

for i in range(len(time_sequence)-1, int(len(time_sequence) / 2), -1):
    current = int(time_sequence[i])
    sum_times2 += current
    if current == 0:
        sum_times2 = 0.8 * sum_times2

if sum_times1 < sum_times2:
    print(f"The winner is left with total time: {sum_times1:.1f}")
else:
    print(f"The winner is right with total time: {sum_times2:.1f}")