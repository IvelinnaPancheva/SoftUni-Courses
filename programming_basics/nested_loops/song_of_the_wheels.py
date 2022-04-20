control_number = int(input())

counter_pw = 0
fourth_pw_found = False
fourth = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and control_number == a * b + c * d:
                    counter_pw += 1
                    print(f"{a}{b}{c}{d}",end = " ")
                    if counter_pw == 4:
                        fourth_pw_found = True
                        fourth = f"{a}{b}{c}{d}"
print()
if fourth_pw_found:
    print(f"Password: {fourth}")
else:
    print("No!")

