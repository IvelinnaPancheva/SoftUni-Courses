code = input().split("|")
message = ""

for digits in code:
    same_digits = [digits[0]]
    total_sum = digits.count("1") * 5 + digits.count("0") * 3

    for x in range(1, len(digits)):
        if digits[x] in same_digits:
            same_digits.append(digits[x])
        else: # different digit is next up
            if len(same_digits) > 1:
                total_sum += len(same_digits)
            same_digits = [digits[x]]
    if len(same_digits) > 1:
        total_sum += len(same_digits)

    message += chr(total_sum)

print(message)