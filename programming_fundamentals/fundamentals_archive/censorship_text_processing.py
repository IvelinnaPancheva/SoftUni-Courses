searched_word = input()
sentence = input()

while searched_word in sentence:
    replacement = len(searched_word) * "*"
    sentence = sentence.replace(searched_word, replacement)

print(sentence)