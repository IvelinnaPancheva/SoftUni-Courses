import re

pattern = r"((?<=\s)([a-z0-9]+[\.\-_a-z0-9])*@([a-z]+)(-[a-z]+)*\.[a-z\.]+)\b"

text = input()

matches = re.findall(pattern, text)

for email in matches:
    print(email[0])