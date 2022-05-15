import math

point1_x = float(input())
point1_y = float(input())
point2_x = float(input())
point2_y = float(input())

distance_center_1 = math.sqrt((point1_x)**2 + (point1_y)**2)
distance_center_2 = math.sqrt((point2_x)**2 + (point2_y)**2)
if distance_center_1 <= distance_center_2:
    print(f"({math.floor(point1_x)}, {math.floor(point1_y)})")
else:
    print(f"({math.floor(point2_x)}, {math.floor(point2_y)})")

