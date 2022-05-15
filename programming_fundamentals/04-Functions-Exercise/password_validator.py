given_password = input()
digit_counter = 0
condition_counter= 0

if 6<= len(given_password) <= 10:
    condition_counter += 1
else:
    print(f"Password must be between 6 and 10 characters")
if given_password.isalnum():
    condition_counter += 1
else:
    print(f"Password must consist only of letters and digits")
for char in given_password:
    if char.isdigit():
        digit_counter += 1
if digit_counter < 2:
    print(f"Password must have at least 2 digits")
else:
    condition_counter += 1
if condition_counter == 3:
    print(f"Password is valid")

