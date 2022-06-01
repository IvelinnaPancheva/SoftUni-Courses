def find_emoticons(string, i):
    emoticon = string[i] + string[i + 1]
    return emoticon


text = input()

for index in range(len(text)):
    if text[index] == ":":
        print(find_emoticons(text, index))