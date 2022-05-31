def sort_chars(text):
    digits = ""
    letters = ""
    others = ""
    for char in text:
        if char.isdigit():
            digits += char
        elif char.isalpha():
            letters += char
        else:
            others += char
    return digits, letters, others


string_sequence = input()

print(sort_chars(string_sequence)[0])
print(sort_chars(string_sequence)[1])
print(sort_chars(string_sequence)[2])
