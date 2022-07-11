import re
text = input()

pattern = r"(?P<number>\d\d*\.?\d*)(?P<letter>[a-zA-Z])"

matches = re.finditer(pattern, text)

for match in matches:
    letter = match.group("letter")
    number = match.group("number")
    start_index = text.index(number)
    end_index = start_index + len(number)

    text = text[0:start_index] + letter + text[end_index:]

print(text)