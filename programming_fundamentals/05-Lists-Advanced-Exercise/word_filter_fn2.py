def even_len_filter(text):
    text = list(filter(lambda word: word if len(word) % 2 == 0 else not word, text))
    text = "\n".join(text)
    return text


current_text = input().split(" ")
current_text = even_len_filter(current_text)
print(current_text)