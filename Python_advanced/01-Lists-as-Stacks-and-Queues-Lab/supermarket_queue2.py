from collections import deque

name = input()
supermarket_queue = deque()

while not name == "End":
    if name != "Paid":
        supermarket_queue.append(name)
    else: # if name == "Paid"
        while supermarket_queue: # while loop i.o. for loop iterating over the len of the queue
            print(supermarket_queue.popleft())
    name = input()

print(f"{len(supermarket_queue)} people remaining.")