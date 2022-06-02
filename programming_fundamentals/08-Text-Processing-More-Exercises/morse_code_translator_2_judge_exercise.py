morse_code_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':' | '}

reversed_morse_code_dict = {value: key for key, value in morse_code_dict.items()}


def text_to_morse_code(text):
    morse_code = []
    text = text.split(" ")
    for word in text:
        for char in word:
            morse_code.append(morse_code_dict[char.upper()])
            morse_code.append(" ")
        morse_code.append(" | ")
    morse_code = "".join(morse_code)
    morse_code = morse_code.strip(" | ")
    return morse_code


def morse_code_to_text(morse_code):
    text = ""
    morse_code = morse_code.split(" | ")
    morse_code = [word.strip() for word in morse_code]
    for word in morse_code:
        word = word.split(" ")
        for char in word:
            text += (reversed_morse_code_dict[char])
        text += " "
    text = text.split(" ")
    text = [word for word in text if word != ""]
    text = " ".join(text)
    return text


morse_code = input()
print(morse_code_to_text(morse_code))
