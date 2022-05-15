def is_prime(n):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True
    else:
        return False


number = int(input())
check = is_prime(number)
print(check)

