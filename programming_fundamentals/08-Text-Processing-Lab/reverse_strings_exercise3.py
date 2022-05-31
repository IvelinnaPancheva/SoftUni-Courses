def reverse_the_word(text):
    return text[::-1]


word = input()

while word != "end":
    print(f"{word} = {reverse_the_word(word)}")
    word = input()

