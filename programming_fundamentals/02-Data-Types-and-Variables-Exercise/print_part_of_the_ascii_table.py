start_num = int(input())
end_num = int(input())

ascii_string = ""

for i in range(start_num, end_num + 1):
    if i < end_num:
        ascii_string += chr(i) + " "
    elif i == end_num:
        ascii_string += chr(i)

print(ascii_string)