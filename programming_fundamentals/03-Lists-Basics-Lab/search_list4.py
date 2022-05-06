n = int(input())
keyword = (input())

string_list = list()

for i in range(n):
    current_word = input()
    string_list.append(current_word)
print(string_list)

for j in range(len(string_list)-1, -1, -1):
    if keyword not in string_list[j]:
        string_list.remove(string_list[j])

print(string_list)