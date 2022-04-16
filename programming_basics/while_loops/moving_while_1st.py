width = int(input())
length = int(input())
height = int(input())

total_free_space = width * length * height
there_is_free_space_left = True # boolean variable to indicate when all the free space is taken

command = input()

while total_free_space > 0:
    if command == "Done":
        break
    else: # command != done
        current_boxes = int(command)
        total_free_space -= current_boxes
        if total_free_space <= 0:
            there_is_free_space_left = False
        else:
            command = input()

if there_is_free_space_left:
    print(f"{total_free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_free_space)} Cubic meters more.")





