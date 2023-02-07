from collections import deque


def max_in_queue(queue):
    if queue:
        print(max(queue))


def serving_orders(queue, quantity):
    while queue:
        if queue[0] <= quantity:
            quantity -= queue[0]
            queue.popleft()
        else:
            break
    return queue


food_quantity = int(input())
orders_line = deque([int(element) for element in input().split()])
max_in_queue(orders_line)

orders_line = serving_orders(orders_line, food_quantity)

if orders_line: # food was not enough, orders not fulfilled
    orders_line = deque(map(str, orders_line))
    print(f'Orders left: {" ".join(orders_line)}')

else: # all orders served
    print("Orders complete")