text = input()

repeated_chars = text[0]
clean_text = ""

for index in range(len(text[1:])):
    char = text[1:][index]
    if char in repeated_chars:
        repeated_chars += char

    else: # different char
        clean_text += repeated_chars[0]
        repeated_chars = char

    if index == len(text[1:]) - 1:
        clean_text += char


print(clean_text)