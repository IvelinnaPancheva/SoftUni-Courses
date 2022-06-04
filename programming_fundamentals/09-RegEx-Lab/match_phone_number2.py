from re import finditer

phone_numbers = input()
pattern = r"\+359([ -])2(\1)\d{3}(\1)\d{4}\b"

matches = finditer(pattern, phone_numbers)
phones = []
for match in matches:
    phone = match.group()
    phones.append(phone)
print(", ".join(phones))