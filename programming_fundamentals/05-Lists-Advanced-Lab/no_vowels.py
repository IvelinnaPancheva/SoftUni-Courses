text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
text = text.lower()
no_vowels = [ch for ch in text if ch not in vowels]

print("".join(no_vowels))