secret_message = input().split(" ")
final_message = list()

for word in secret_message:
    char_list = list(word)
    ascii_code = ""
    for char in char_list:
        if 48 <= ord(char) <= 57:
            ascii_code += char
    char_list = [char for char in char_list if char not in list(ascii_code)]
    first_letter = chr(int(ascii_code))
    char_list[0], char_list[-1] = char_list[-1], char_list[0]
    new_word = first_letter + "".join(char_list)
    final_message.append(new_word)

print(" ".join(final_message))

