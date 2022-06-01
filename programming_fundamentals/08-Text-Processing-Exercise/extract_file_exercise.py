path = input().split(chr(92))
file_name = (path[-1]).split(".")

print(f"File name: {file_name[0]}\nFile extension: {file_name[1]}")
