n = int(input())
l = int(input())

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(97, 97 + l):
            for d in range(97, 97 + l):
                for e in range(1, n + 1):
                    if e > a and e > b:
                        c_char = chr(c)
                        d_char = chr(d)
                        print(f"{a}{b}{c_char}{d_char}{e}", end= " ")