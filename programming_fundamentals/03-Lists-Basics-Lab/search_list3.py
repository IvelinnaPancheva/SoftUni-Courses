n = int(input())
keyword = (input())

string_list = list()
filtered_list = list()

for i in range(n):
    current_word = input()
    string_list.append(current_word)
    filtered_list.append(current_word)
    if keyword not in string_list[i]:
        filtered_list.remove((string_list[i]))

print(string_list)
print(filtered_list)