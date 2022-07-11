import re


def destroy_the_mines(string):  # text variable argument => parameter string
    pattern = r"<[\W\w]{2}>"

    matches = re.findall(pattern, string)

    for match in matches:
        first_char = match[1]
        second_char = match[2]
        n = abs(ord(first_char) - ord(second_char))
        start_index = string.index(match)
        end_index = start_index + 4  # exclusive
        substring_to_replace = ""
        for i in range(start_index - n, end_index + n):
            if 0 <= i < len(string):
                substring_to_replace += string[i]

        replacement = len(substring_to_replace) * "_"
        string = string.replace(substring_to_replace, replacement)

    return string


text = input()
print(destroy_the_mines(text))
