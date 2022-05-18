text = input().split(" ")
text = list(filter(lambda word: word if len(word) % 2 == 0 else not word, text))
text = "\n".join(text)
print(text)