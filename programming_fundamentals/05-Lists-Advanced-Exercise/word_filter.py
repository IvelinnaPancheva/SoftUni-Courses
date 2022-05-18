text = input().split(" ")
text = [word for word in text if len(word) % 2 == 0]
text = "\n".join(text)
print(text)