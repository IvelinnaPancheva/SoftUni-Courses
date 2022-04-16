n = int(input())

left_sum = 0
right_sum = 0

for i in range(1, n+1):
    left_number = int(input())
    left_sum += left_number
for i in range(n + 1, (2 * n+1)):
    right_number = int(input())
    right_sum += right_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")

