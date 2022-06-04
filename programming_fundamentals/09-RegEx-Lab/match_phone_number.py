import re

phone_numbers = input()
pattern = r"\+359([ -])2(\1)\d{3}(\1)\d{4}\b"

matches = re.finditer(pattern, phone_numbers)

list_of_matches = []
for match in matches:
    start = match.start()
    end = match.end()
    phone = phone_numbers[start:end]
    list_of_matches.append(phone)

list_of_matches = ", ".join(list_of_matches)
print(list_of_matches)