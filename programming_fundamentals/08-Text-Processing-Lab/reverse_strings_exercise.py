word = input()

while word != "end":
    reversed_word = "".join(reversed(word))
    print(f"{word} = {reversed_word}")
    word = input()

