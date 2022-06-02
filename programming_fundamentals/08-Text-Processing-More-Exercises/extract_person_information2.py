def extract_name(text):
    at_position = text.index("@")
    pipe_position = text.index("|")
    name = text[at_position + 1:pipe_position]
    return name


def extract_age(text):
    hash_position = text.index("#")
    asterisk_position = text.index("*")
    age = text[hash_position+1:asterisk_position]
    persons[name] = age
    return age


n= int(input())
persons = {}

for _ in range(n):
    text = input()
    current_name = extract_name(text)
    current_age = extract_age(text)
    persons[current_name] = current_age

for name, age in persons.items():
    print(f"{name} is {age} years old.")


