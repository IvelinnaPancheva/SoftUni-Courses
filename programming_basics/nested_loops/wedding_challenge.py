men = int(input())
women = int(input())
tables = int(input())
seats = tables * 2

while seats >= 0:
    for man in range(1, men + 1):
        for woman in range(1, women + 1):
            print(f"({man} <-> {woman})", end=" ")
            seats -= 2
            if seats > men * women:
                break