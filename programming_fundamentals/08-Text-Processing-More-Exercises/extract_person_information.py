n= int(input())
persons = {}

for _ in range(n):
    text = input()
    at_position = text.index("@")
    pipe_position = text.index("|")
    name = text[at_position+1:pipe_position]

    hash_position = text.index("#")
    asterisk_position = text.index("*")
    age = text[hash_position+1:asterisk_position]
    persons[name] = age

for name, age in persons.items():
    print(f"{name} is {age} years old.")


