import re

number_keys = input().split(" ")

text = input()
while text != "find":
    start_index = 0
    end_index = start_index + len(number_keys)
    decrypted_text = ""

    while start_index < len(text):
        partial = text[start_index:end_index]
        for index in range(len(partial)):
            for i in range(len(number_keys)):
                if index == i:
                    char = ord(partial[index]) - int(number_keys[index])
                    char = chr(char)
                    decrypted_text += char
        start_index += len(number_keys)
        end_index += len(number_keys)

    # print(decrypted_text)

    treasure_pattern = r"(?<=&)[a-zA-Z]+(?=&)"
    coordinates_pattern = r"(?<=<)[A-Za-z0-9]+(?=>)"

    treasure_match = re.findall(treasure_pattern, decrypted_text)
    coordinates_match = re.findall(coordinates_pattern, decrypted_text)

    treasure = "".join(treasure_match)
    coordinates = "".join(coordinates_match)

    print(f"Found {treasure} at {coordinates}")

    text = input()



