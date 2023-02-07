from collections import deque

clothes_stack = deque(int(element) for element in input().split())
capacity_per_rack = int(input())
rack_counter = 1
taken_capacity = 0

while clothes_stack:
    if clothes_stack[-1] + taken_capacity < capacity_per_rack:
        taken_capacity += clothes_stack[-1]
    elif clothes_stack[-1] + taken_capacity == capacity_per_rack:
        taken_capacity = 0
        rack_counter += 1
    else: # clothes_stack[-1] + taken_capacity > capacity_per_rack
        rack_counter += 1
        taken_capacity = clothes_stack[-1]
    clothes_stack.pop()

if taken_capacity == 0:
    print(rack_counter-1)
else:
    print(rack_counter)

