import re

text = input()

pattern = r"<[\W\w]{2}>"

matches = re.findall(pattern, text)

for match in matches:
    first_char = match[1]
    second_char = match[2]
    n = abs(ord(first_char) - ord(second_char))
    start_index = text.index(match)
    end_index = start_index + 4 # exclusive
    substring_to_replace = ""
    for i in range(start_index-n, end_index+n):
        if 0 <= i < len(text):
            substring_to_replace += text[i]

    replacement = len(substring_to_replace) * "_"
    text = text.replace(substring_to_replace, replacement)

print(text)
