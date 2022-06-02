def sum_ascii_values(first_symbol, second_symbol, given_text):
    total_sum = 0
    for number in range(ord(first_symbol) + 1, ord(second_symbol)):
        for char in given_text:
            if ord(char) == number:
                total_sum += ord(char)
    return total_sum


first_char = input()
second_char = input()
text = input()
print(sum_ascii_values(first_char, second_char, text))