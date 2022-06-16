import re

text = input().lower()
searched_word = input().lower()

pattern = fr"\b{searched_word}\b"

matches = re.findall(pattern, text)

print(len(matches))