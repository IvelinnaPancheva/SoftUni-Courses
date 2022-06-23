import re

n = int(input())

key_chars = ["s", "t", "a", "r"]

attacked = []
destroyed = []
for _ in range(n):
    encrypted_text = input()
    key = 0
    for char in encrypted_text:
        if char.lower() in key_chars:
            key += 1

    decrypted_text = ""
    for char in encrypted_text:
        new_char = chr(ord(char) - key)
        decrypted_text += new_char

    message_pattern = r"@(?P<planet>[A-Z][a-z]+)([^@\-!:>]*):(?P<population>\d+)([^@\-!:>]*)!(?P<type>A|D)!([^@\-!:>]*)\->(?P<count>\d+)([^@\-!:>0-9]*)"

    matches = re.finditer(message_pattern, decrypted_text)
    if matches:
        for match in matches:
            planet = match.group("planet")
            population = int(match.group("population"))
            type_attack = match.group("type")
            count = int(match.group("count"))
            if type_attack == "A":
                attacked.append(planet)
            elif type_attack == "D":
                destroyed.append(planet)
    attacked = sorted(attacked)
    destroyed = sorted(destroyed)

print(f"Attacked planets: {len(attacked)}")
for planet in attacked:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed)}")
for planet in destroyed:
    print(f"-> {planet}")
