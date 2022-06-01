def extract_file_name(pathname):
    file_name = (pathname[-1]).split(".")
    return f"File name: {file_name[0]}\nFile extension: {file_name[1]}"


path = input().split(chr(92))

print(extract_file_name(path))
