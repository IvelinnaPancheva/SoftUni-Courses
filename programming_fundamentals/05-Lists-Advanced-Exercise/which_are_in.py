first_sequence = input().split(", ")
second_sequence = input().split(", ")
substring_list = []

for string in first_sequence:
    for word in second_sequence:
        if string in word:
            if string not in substring_list:
                substring_list.append(string)

print(substring_list)