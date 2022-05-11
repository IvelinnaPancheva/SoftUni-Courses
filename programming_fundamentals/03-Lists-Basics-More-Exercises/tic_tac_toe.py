first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")

first_line.extend(second_line)
first_line.extend(third_line)

first_player_win = False
second_player_win = False
draw = False

for i in range(len(first_line)):
    if first_line[0] == first_line[1] == first_line[2] == "1" or \
        first_line[3] == first_line[4] == first_line[5] == "1" or \
        first_line[6] == first_line[7] == first_line[8] == "1" or \
        first_line[0] == first_line[3] == first_line[6] == "1" or \
        first_line[1] == first_line[4] == first_line[7] == "1" or \
        first_line[2] == first_line[5] == first_line[8] == "1" or \
        first_line[0] == first_line[4] == first_line[8] == "1" or \
            first_line[2] == first_line[4] == first_line[6] == "1":
        first_player_win = True
    elif first_line[0] == first_line[1] == first_line[2] == "2" or \
        first_line[3] == first_line[4] == first_line[5] == "2" or \
        first_line[6] == first_line[7] == first_line[8] == "2" or \
        first_line[0] == first_line[3] == first_line[6] == "2" or \
        first_line[1] == first_line[4] == first_line[7] == "2" or \
        first_line[2] == first_line[5] == first_line[8] == "2" or \
        first_line[0] == first_line[4] == first_line[8] == "2" or \
            first_line[2] == first_line[4] == first_line[6] == "2":
        second_player_win = True
    else:
        draw = True

if first_player_win:
    print("First player won")
elif second_player_win:
    print("Second player won")
else:
    print("Draw!")

