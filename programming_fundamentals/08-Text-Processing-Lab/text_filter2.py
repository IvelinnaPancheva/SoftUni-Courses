def filter_of_banned(banned_words, words):
    for word in banned_words:
        while word in words:
            words = words.replace(word, "*" * len(word))

    return words


ban_list = input().split(", ")
text = input()
text = filter_of_banned(ban_list, text)
print(text)