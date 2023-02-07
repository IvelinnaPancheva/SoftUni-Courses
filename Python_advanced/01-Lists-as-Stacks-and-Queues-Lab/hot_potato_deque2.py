from time import time
from collections import deque

start = time()

kids = deque(input().split(" "))
n = int(input())

# print(kids)

while len(kids) > 1:
    kids.rotate(-n)
    print(f"Removed {kids.pop()}")

print(f"Last is {kids.pop()}")
print(f'Time taken to run: {time() - start} seconds')
