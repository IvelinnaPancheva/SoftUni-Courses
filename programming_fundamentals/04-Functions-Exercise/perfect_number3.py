def is_number_perfect(number):
    sum_of_divisors = 0
    for num in range(1, number):
        if number % num == 0:
            sum_of_divisors += num
    if sum_of_divisors == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


current_number = int(input())
is_number_perfect(current_number)