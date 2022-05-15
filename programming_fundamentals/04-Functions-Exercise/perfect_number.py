def is_number_perfect(number):
    sum_of_divisors = 0
    for num in range(1, number):
        if number % num == 0:
            sum_of_divisors += num
    if sum_of_divisors == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


current_number = int(input())
message = is_number_perfect(current_number)
print(message)