import math


def closer_to_center(a1, a2, b1, b2):
    distance_center_a = math.sqrt(a1**2 + a2**2)
    distance_center_b = math.sqrt(b1**2 + b2**2)
    if distance_center_a <= distance_center_b:
        return f"({math.floor(a1)}, {math.floor(a2)})"
    else:
        return f"({math.floor(b1)}, {math.floor(b2)})"


point1_x = float(input())
point1_y = float(input())
point2_x = float(input())
point2_y = float(input())
print(closer_to_center(point1_x, point1_y, point2_x, point2_y))
