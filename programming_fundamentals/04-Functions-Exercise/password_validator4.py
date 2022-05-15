def len_validation(password):
    if 6 > len(password) or len(password) > 10:
        print(f"Password must be between 6 and 10 characters")
    else:
        return True


def char_validation(password):
    if not password.isalnum():
        print(f"Password must consist only of letters and digits")
    else:
        return True


def digit_validation(password):
    digit_counter = 0
    for char in password:
        if char.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print(f"Password must have at least 2 digits")
    else:
        return True


def password_validation(password):
    is_len_valid = len_validation(password)
    is_char_valid = char_validation(password)
    is_digit_valid = digit_validation(password)
    if is_len_valid and is_char_valid and is_digit_valid:
        print(f"Password is valid")


given_password = input()
password_validation(given_password)

