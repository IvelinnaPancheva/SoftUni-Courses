map = input()
hideout_not_found = True

while hideout_not_found:
    clues = input().split(" ")
    character = clues[0]
    min_count = int(clues[1])
    expression = character * min_count

    if expression in map:
        index = map.index(expression)
        length = len(expression)
        for i in range(index+length, len(map)):
            if map[i] == character:
                length += 1
            else:
                break

        hideout_not_found = False
        print(f"Hideout found at index {index} and it is with size {length}!")
        break
