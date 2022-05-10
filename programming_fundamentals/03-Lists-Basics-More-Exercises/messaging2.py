sequence_of_numbers = input().split(" ")
chars_string = list(input())
sum_var = 0
message = ""

for num in sequence_of_numbers:
    sum_var = 0
    for i in range(len(num)):
        sum_var += int(num[i])

    if sum_var <= len(chars_string):
        for j in range(len(chars_string)):
            if j == sum_var:
                message += chars_string[j]
                chars_string.remove(chars_string[j])
                break
    else: # sumvar > len(chars_string)
        sum_var -= (sum_var // len(chars_string)) * len(chars_string)
        for j in range(len(chars_string)):
            if j == sum_var:
                message += chars_string[j]
                chars_string.remove(chars_string[j])
                break

print(message)
