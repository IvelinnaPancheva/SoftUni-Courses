from collections import deque
elements = deque(input().split(" "))
step = int(input())
removed = []

while elements:
    elements.rotate(-step)
    removed.append(elements.pop())

# print(elements)
removed = ",".join(removed)
print(f"[{removed}]")