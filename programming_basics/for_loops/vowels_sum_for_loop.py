text = input()

vowels_sum = 0

for symbol in text:
    if symbol == "a":
        vowels_sum += 1
    elif symbol == "e":
        vowels_sum += 2
    elif symbol == "i":
        vowels_sum += 3
    elif symbol == "o":
        vowels_sum += 4
    elif symbol == "u":
        vowels_sum += 5

print(vowels_sum)