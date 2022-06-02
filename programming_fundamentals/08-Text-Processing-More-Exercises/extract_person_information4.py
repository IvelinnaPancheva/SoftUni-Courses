import re

n= int(input())
persons = {}

for _ in range(n):
    text = input()
    name_pattern = r"(?<=@)[a-zA-Z]+(?=|)"
    age_pattern = r"(?<=#)\d+(?=\*)"
    name = re.findall(name_pattern, text)
    age = re.findall(age_pattern, text)
    name = "".join(name)
    age = "".join(age)

    if name not in persons.keys():
        persons[name] = age

for name, age in persons.items():
    print(f"{name} is {age} years old.")


