email = input()

if "@" in email:
    index = email.index("@")
    before_part = email[0:index]
    after_part = email[index+1:]
    before_sum = 0
    after_sum = 0
    for char in before_part:
        before_sum += ord(char)
    for char in after_part:
        after_sum += ord(char)
    if before_sum - after_sum >= 0:
        print("Call her!")

    else:
        print("She is not the one.")
