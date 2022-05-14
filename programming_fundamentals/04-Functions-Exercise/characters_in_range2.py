def print_chars_in_range(char_one, char_two):
    final_string = ""
    for character in range(ord(char_one)+1, ord(char_two)):
        final_string += chr(character) + " "
    return final_string


first_char = input()
second_char = input()
output_string = print_chars_in_range(first_char, second_char)
print(output_string)