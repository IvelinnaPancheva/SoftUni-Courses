text = ""
word = ""

c_counter = 0
o_counter = 0
n_counter = 0

command = str(input())

while command != "End":
    if command.isalpha():

        if command == "c":
            c_counter += 1

            if c_counter > 1:
                text += command
                c_counter = 1

        elif command == "o":
            o_counter += 1
            if o_counter > 1:
                text += command
                o_counter = 1

        elif command == "n":
            n_counter += 1
            if n_counter > 1:
                text += command
                n_counter = 1

        else:
            text += command

    if (c_counter + n_counter + o_counter) == 3:
        text += " "
        word = text
        c_counter = 0
        n_counter = 0
        o_counter = 0

    else:
        text += ""

    if command == "End":
        break
    command = str(input())

print(word)




