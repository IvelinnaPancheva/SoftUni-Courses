remove_substring = input()
char_sequence = input()

while remove_substring in char_sequence:
    char_sequence = char_sequence.replace(remove_substring, "")

print(char_sequence)