text = input()
the_list = []

for i in range(len(text)):
    if 65 <= ord(text[i]) <= 90:
        the_list.append(int(i))

print(the_list)
