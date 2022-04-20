last_sector = input()
rows_sector_a = int(input())
odd_row_seats = int(input())

# even row seats = odd row seats + 2
total_sectors = ord(last_sector) - 64
total_seats = 0

for i in range(65, ord(last_sector) + 1):
    sector = chr(i)
    rows_sector_a += 1
    for j in range(1, rows_sector_a):
        if j % 2 == 1:
            for x in range(1, odd_row_seats + 1):
                seat = chr(96 + x)
                print(f"{sector}{j}{seat}")
                total_seats += 1
        else:
            for y in range(1, odd_row_seats + 3):
                seat = chr(96 + y)
                print(f"{sector}{j}{seat}")
                total_seats += 1

print(total_seats)