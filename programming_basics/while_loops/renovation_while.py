from math import ceil

height = int(input())
width = int(input())
percent_tobe_excluded = int(input())

area = 4 * height * width
area_painting = ceil(area - percent_tobe_excluded / 100 * area)

command = input()
while command != "Tired!":
    current_paint = int(command)
    area_painting -= current_paint
    if area_painting < 0:
        print(f"All walls are painted and you have {abs(area_painting)} l paint left!")
        break
    elif area_painting == 0:
        print(f"All walls are painted! Great job, Pesho!")
        break
    command = input()

if command == "Tired!":
    print(f"{area_painting} quadratic m left.")




# На следващите редове до получаване на командата "Tired!" или докато не бъдат боядисани всички стени, се чете по едно число:
# Литри боя – цяло число [0…100]: