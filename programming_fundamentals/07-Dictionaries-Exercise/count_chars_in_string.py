words = input()
characters = {}

for char in words:
    if char not in characters and char != " ":
        count = words.count(char)
        characters[char] = count
        print(f"{char} -> {characters[char]}")

