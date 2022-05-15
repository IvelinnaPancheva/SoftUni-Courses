given_password = input()
digit_counter = 0

if 6 > len(given_password) or len(given_password) > 10:
    print(f"Password must be between 6 and 10 characters")
if not given_password.isalnum():
    print(f"Password must consist only of letters and digits")
for char in given_password:
    if char.isdigit():
        digit_counter += 1
if digit_counter < 2:
    print(f"Password must have at least 2 digits")

if 6 <= len(given_password) <= 10 and given_password.isalnum() and digit_counter >= 2:
    print(f"Password is valid")

