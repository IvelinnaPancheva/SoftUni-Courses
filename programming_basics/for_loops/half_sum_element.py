import sys

n = int(input())

max_num = -sys.maxsize
sum_of_num = 0

for number in range(1, n + 1):
    number = int(input())
    sum_of_num += number
    if number > max_num:
        max_num = number

if sum_of_num - max_num == max_num:
    print("Yes")
    print(f"Sum = {max_num}")

else:
    diff = abs(max_num - (sum_of_num - max_num))
    print("No")
    print(f"Diff = {diff}")



