n = int(input())

for i in range(n):
    a = chr(97 + i)
    for j in range(n):
        b = chr(97 + j)
        for x in range(n):
            c = chr(97 + x)
            print(f'{a}{b}{c}')
