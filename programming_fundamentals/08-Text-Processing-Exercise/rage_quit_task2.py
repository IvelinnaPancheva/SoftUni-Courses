def unique_symbols_sequence(text):
    unique_symbols = ''
    for char in text:
        if not char.isnumeric():
            if char.upper() not in unique_symbols:
                unique_symbols += char.upper()
    return  len(unique_symbols)


def rage_message_string(text):
    rage_message = ''
    temporary = ''
    number = ''
    for index in range(len(text)):
        if not text[index].isnumeric():
            temporary += text[index].upper()
        else: # text[index] is numeric, check next chars for digits
            number = text[index]
            for i in range(index+1, len(text)):
                if not text[i].isnumeric():
                    break
                else:
                    number += text[i]
            number = int(number)
            rage_message += number * temporary
            temporary = ''
    return rage_message


message = input()

n_unique_chars = unique_symbols_sequence(message)
rage_message = rage_message_string(message)
print(f"Unique symbols used: {n_unique_chars}")
print(rage_message)
