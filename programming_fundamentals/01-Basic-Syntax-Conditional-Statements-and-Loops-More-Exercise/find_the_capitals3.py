def find_the_capitals(text):
    the_list = []
    for i in range(len(text)):
        if 65 <= ord(text[i]) <= 90:
            the_list.append(int(i))
    return the_list


current_text = input()
print(find_the_capitals(current_text))
