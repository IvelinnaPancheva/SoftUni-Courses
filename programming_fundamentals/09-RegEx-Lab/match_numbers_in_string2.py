import re

text = input()

pattern = r"(^|(?<=\s))-?([0]|([1-9][0-9]*))(\.[0-9]+)?($|(?=\s))"

matches = re.finditer(pattern, text)

matching_nums = []
for match in matches:
    matching_nums.append(match.group())

print(" ".join(matching_nums))