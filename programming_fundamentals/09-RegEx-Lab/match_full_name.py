import re

full_names = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

matches = re.findall(pattern, full_names)

matches = " ".join(matches)
print(matches)