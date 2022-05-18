version = input().split(".")
version = list(map(int, version))

for index in range(len(version) - 1, -1, -1):
    if index == len(version)-1:
        version[index] += 1
        if version[index] == 10:
            version[index] = 0
            version[index-1] += 1
            if version[index-1] == 10:
                version[index - 1] = 0
                version[index -2] += 1
version = list((map(str, version)))
print(".".join(version))