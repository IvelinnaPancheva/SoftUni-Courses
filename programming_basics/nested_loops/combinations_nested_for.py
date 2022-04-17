number = int(input())

combinations_cnt = 0

for x in range(0, number + 1):
    for y in range(0, number + 1):
        for z in range(0, number + 1):
            if x + y + z == number:
                combinations_cnt += 1

print(combinations_cnt)
