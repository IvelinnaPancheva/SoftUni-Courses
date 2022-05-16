from math import sqrt, floor


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_center_distance = sqrt(x1 ** 2 + y1 ** 2)
    second_center_distance = sqrt(x2 ** 2 + y2 ** 2)
    third_center_distance = sqrt(x3 ** 2 + y3 ** 2)
    fourth_center_distance = sqrt(x4 ** 2 + y4 ** 2)

    first_second_line = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    third_fourth_line = sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)

    if first_second_line >= third_fourth_line:
        if first_center_distance <= second_center_distance:
            return f"({floor(a1)}, {floor(a2)})({floor(b1)}, {floor(b2)})"
        else:
            return f"({floor(b1)}, {floor(b2)})({floor(a1)}, {floor(a2)})"
    else:
        if third_center_distance <= fourth_center_distance:
            return f"({floor(c1)}, {floor(c2)})({floor(d1)}, {floor(d2)})"
        else:
            return f"({floor(d1)}, {floor(d2)})({floor(c1)}, {floor(c2)})"


a1 = float(input())
a2 = float(input())
b1 = float(input())
b2 = float(input())
c1 = float(input())
c2 = float(input())
d1 = float(input())
d2 = float(input())

print(longer_line(a1, a2, b1, b2, c1, c2, d1, d2))