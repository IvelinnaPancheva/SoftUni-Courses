def password_validation(password):
    digit_counter = 0
    if 6 > len(password) or len(password) > 10:
        print(f"Password must be between 6 and 10 characters")
    if not password.isalnum():
        print(f"Password must consist only of letters and digits")
    for char in password:
        if char.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print(f"Password must have at least 2 digits")

    if 6 <= len(password) <= 10 and password.isalnum() and digit_counter >= 2:
        print(f"Password is valid")


given_password = input()
password_validation(given_password)
