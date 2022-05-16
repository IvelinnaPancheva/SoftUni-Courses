def no_vowels(text):
    vowels = ['a', 'o', 'u', 'e', 'i']
    text = text.lower()
    no_vowels = [ch for ch in text if ch not in vowels]
    return "".join(no_vowels)


current_text = input()
print(no_vowels(current_text))