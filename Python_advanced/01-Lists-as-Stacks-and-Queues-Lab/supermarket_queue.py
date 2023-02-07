from collections import deque

name = input()
supermarket_queue = deque()

while not name == "End":
    if name != "Paid":
        supermarket_queue.append(name)
    else: # if name == "Paid"
        for index in range(len(supermarket_queue)):
            print(supermarket_queue.popleft())
    name = input()

print(f"{len(supermarket_queue)} people remaining.")