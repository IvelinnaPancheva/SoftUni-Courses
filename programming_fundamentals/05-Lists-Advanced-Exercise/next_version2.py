version = input().split(".")
version = list(map(int, version))
version[-1] += 1

for index in range(len(version) - 1, -1, -1):
    if version[index] == 10 and index != 0:
        version[index] = 0
        version[index-1] += 1

version = list((map(str, version)))
print(".".join(version))