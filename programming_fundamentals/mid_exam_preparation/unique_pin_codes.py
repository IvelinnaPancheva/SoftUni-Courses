def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


first_upper_limit = int(input())
second_upper_limit = int(input())
third_upper_limit = int(input())

for x in range(1, first_upper_limit + 1):
    for y in range(2, second_upper_limit + 1):
        for z in range(1, third_upper_limit + 1):
            if x % 2 == 0 and z % 2 == 0 and is_prime(y):
                pin = f"{x} {y} {z}"
                print(pin)