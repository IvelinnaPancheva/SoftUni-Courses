length = int(input())
width = int(input())

cake_pieces = length * width
total_eaten_pieces = 0
cake_is_eaten = False

command = input()

while cake_pieces > total_eaten_pieces:
    if command != "STOP":
        current_pieces = int(command)
        total_eaten_pieces += current_pieces

        if total_eaten_pieces >= cake_pieces:
            cake_is_eaten = True
        else:
            command = input()

    else: # command == STOP
        break


diff = abs(cake_pieces - total_eaten_pieces)

if cake_is_eaten:
    print(f"No more cake left! You need {diff} pieces more.")
else: # cake pieces are left
    print(f"{diff} pieces are left.")