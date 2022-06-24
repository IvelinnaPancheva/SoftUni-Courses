numbers = input().split(" ")
modifications = input().split(" ")
modifications = [int(x) for x in modifications]
modified_list = []

for x in range(modifications[0]):
    modified_list.append(numbers[x])

for x in range(modifications[1]):
    modified_list.pop(0)

if str(modifications[2]) in modified_list:
    print("YES!")
else:
    print("NO!")
