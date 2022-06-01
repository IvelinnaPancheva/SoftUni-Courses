message = input()
unique_symbols = ''
rage_message = ''
temporary = ''
number = ''

for index in range(len(message)):
    if message[index].isnumeric():
        number = message[index]
        for i in range(index+1, len(message)):
            if message[i].isnumeric():
                number += message[i]
            else:
                break
        number = int(number)
        rage_message += number * temporary
        temporary = ""
    else: # non numeric char, check if unique, add to temporary for multiplying
        if message[index].upper() not in unique_symbols:
            unique_symbols += message[index].upper()
        temporary += message[index].upper()

print(f"Unique symbols used: {len(unique_symbols)}")
print(rage_message)
