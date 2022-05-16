from math import sqrt, floor

a1 = float(input())
a2 = float(input())
b1 = float(input())
b2 = float(input())
c1 = float(input())
c2 = float(input())
d1 = float(input())
d2 = float(input())

a_center_distance = sqrt(a1**2 + a2**2)
b_center_distance = sqrt(b1**2 + b2**2)
c_center_distance = sqrt(c1**2 + c2**2)
d_center_distance = sqrt(d1**2 + d2**2)

ab = sqrt((b1 - a1)**2 + (b2 - a2)**2)
cd = sqrt((c1 - d1)**2 + (c2 - d2)**2)

if ab >= cd:
    if a_center_distance <= b_center_distance:
        print(f"({floor(a1)}, {floor(a2)})({floor(b1)}, {floor(b2)})")
    else:
        print(f"({floor(b1)}, {floor(b2)})({floor(a1)}, {floor(a2)})")
else:
    if c_center_distance <= d_center_distance:
        print(f"({floor(c1)}, {floor(c2)})({floor(d1)}, {floor(d2)})")
    else:
        print(f"({floor(d1)}, {floor(d2)})({floor(c1)}, {floor(c2)})")
