n = int(input())
word = (input())

string_list = list()
filtered_list = list()

for i in range(n):
    string_list.append(input())

for j in range(len(string_list)):
    if word in string_list[j]:
        filtered_list.append(string_list[j])

print(string_list)
print(filtered_list)