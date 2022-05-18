def check_string_for_substring(first_sequence, second_sequence):
    substring_list = []
    for string in first_sequence:
        for word in second_sequence:
            if string in word and string not in substring_list:
                substring_list.append(string)
    return substring_list


current_first_sequence = input().split(", ")
current_second_sequence = input().split(", ")
current_substring_list = check_string_for_substring(current_first_sequence, current_second_sequence)
print(current_substring_list)