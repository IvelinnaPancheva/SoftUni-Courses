numbers_string = input()
n = int(input())
list_variable = numbers_string.split(" ")
integer_list = list()
new_list = []

for element in list_variable:
    integer_list.append(int(element))

for i in range(n):
    integer_list.remove(min(integer_list))

for element in integer_list:
    element = str(element)
    new_list.append(element)

numbers_string = ", ".join(new_list)

print(numbers_string)