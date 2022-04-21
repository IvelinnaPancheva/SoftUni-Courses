n = int(input())
for row in range(1, n+1):
    for column in range(row, row+1):
        print(f"$ " * column)
