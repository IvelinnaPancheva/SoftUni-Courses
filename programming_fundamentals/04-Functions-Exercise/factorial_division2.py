def factorial_division_function(a, b):
    first_factorial = 1
    second_factorial = 1
    for num in range(2, a + 1):
        first_factorial *= num
    for num in range(2, b+ + 1):
        second_factorial *= num
    return first_factorial / second_factorial

first_number = int(input())
second_number = int(input())
print(f"{factorial_division_function(first_number, second_number):.2f}")
