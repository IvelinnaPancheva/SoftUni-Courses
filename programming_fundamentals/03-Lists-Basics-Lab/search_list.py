n = int(input())
word = (input())

string_list = list()
filtered_list = list()

for i in range(n):
    string_list.append(input())
    if word in string_list[i]:
        filtered_list.append((string_list[i]))

print(string_list)
print(filtered_list)