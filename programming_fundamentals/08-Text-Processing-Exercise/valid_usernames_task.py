usernames = input().split(", ")

for username in usernames:
    if 3 <= len(username) <= 16:
        username_is_invalid = False
        for char in username:
            if char.isalnum() or char == "_" or char == "-":
                continue
            else:
                username_is_invalid = True
                break
        if not username_is_invalid:
            print(username)
