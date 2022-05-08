numbers_string = input()
n = int(input())
list_variable = numbers_string.split(" ")
integer_list = list_variable.copy()
new_list = []

for i in range(len(integer_list)):
    integer_list[i] = int(integer_list[i])

for i in range(n):
    integer_list.remove(min(integer_list))

for element in integer_list:
    element = str(element)
    new_list.append(element)

numbers_string = ", ".join(new_list)

print(numbers_string)