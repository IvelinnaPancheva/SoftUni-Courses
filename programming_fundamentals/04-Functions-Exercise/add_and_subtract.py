def sum_numbers(a, b):
    sum = a + b
    return sum

def subtract(sum, c):
    return sum - c

def add_and_subtract(a, b, c):
    sum_of_a_b = sum_numbers(a, b)
    result = subtract(sum_of_a_b, c)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())
answer = add_and_subtract(first_num, second_num, third_num)
print(answer)