text = input()
chars_to_skip = 0
text_to_print = ""

for i in range(len(text)):
    if text[i] == '>':
        chars_to_skip += int(text[i+1])
        text_to_print += text[i]

    elif text[i] != '>' and chars_to_skip == 0:
        text_to_print += text[i]

    elif text[i] != '>' and chars_to_skip > 0:
        chars_to_skip -= 1

print(text_to_print)