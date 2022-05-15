def is_number_perfect(number):
    sum_of_divisors = 0
    for num in range(1, number+1):
        if number % num == 0:
            sum_of_divisors += num
    if sum_of_divisors // 2 == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


current_number = int(input())
print(is_number_perfect(current_number))