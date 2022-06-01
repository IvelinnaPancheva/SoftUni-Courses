def length_is_valid(text):
    if 3 <= len(text) <= 16:
        return True
    return False


def allowed_chars_only(text):
    for char in text:
        if not (char.isalnum() or char == "_" or char == "-"):
            return False
    return True


def no_whitespaces(text):
    for char in text:
        if char == " ":
            return False
    return True


def username_is_valid(text):
    if length_is_valid(text) and allowed_chars_only(text) and no_whitespaces(text):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)
