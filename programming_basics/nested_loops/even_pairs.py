def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


first_pair_lower_limit = int(input())
second_pair_lower_limit = int(input())
range_first_pair = int(input())
range_second_pair = int(input())

first_pair_upper_limit = first_pair_lower_limit + range_first_pair
second_pair_upper_limit = second_pair_lower_limit + range_second_pair

for x in range(first_pair_lower_limit, first_pair_upper_limit+1):
    for y in range(second_pair_lower_limit, second_pair_upper_limit+1):
        if is_prime(x) and is_prime(y):
            left_pair = x
            right_pair = y
            print(f"{x}{y}")
