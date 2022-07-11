def find_the_hideout(string):

    while True:
        clues = input().split(" ")
        character = clues[0]
        min_count = int(clues[1])
        expression = character * min_count

        if expression in string:
            index = string.index(expression)
            length = len(expression)
            for i in range(index + length, len(string)):
                if string[i] == character:
                    length += 1
                else:
                    break

            return f"Hideout found at index {index} and it is with size {length}!"


map = input()  # parameter = string in function def
print(find_the_hideout(map))
