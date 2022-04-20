# ABxyBA password template

a = int(input())
b = int(input())
maximum_passwords = int(input())
password_counter = 0
ord_uppercase_a = 35
ord_uppercase_b = 64
max_pw_reached = False

for x in range(1, a+1):
    if max_pw_reached:
        break
    for y in range(1, b+1):
        current_password = chr(ord_uppercase_a) + chr(ord_uppercase_b) + str(x) + str(y) + chr(ord_uppercase_b) \
                           + chr(ord_uppercase_a)

        password_counter += 1
        if password_counter == maximum_passwords+1:
            max_pw_reached = True
            break

        else:
            print(current_password, end="|")
            ord_uppercase_a += 1
            if ord_uppercase_a >55:
                ord_uppercase_a = 35
            ord_uppercase_b += 1
            if ord_uppercase_b > 96:
                ord_uppercase_b = 64

