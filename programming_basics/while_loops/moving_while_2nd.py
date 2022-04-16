width = int(input())
length = int(input())
height = int(input())

total_free_space = width * length * height
taken_free_space = 0  # counter to collect the volume of boxes
there_is_free_space_left = True # boolean variable to indicate when all the free space is taken

command = input()

while total_free_space > taken_free_space:
    if command == "Done":
        break
    else: # command != done
        current_boxes = int(command)
        taken_free_space += current_boxes
        if taken_free_space >= total_free_space:
            there_is_free_space_left = False
        else:
            command = input()

diff = abs(total_free_space - taken_free_space)
if there_is_free_space_left == False:
    print(f"No more free space! You need {diff} Cubic meters more.")

else:
    print(f"{diff} Cubic meters left.")





