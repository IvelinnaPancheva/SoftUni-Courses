import collections

food_quantity = int(input())
orders_line = collections.deque([int(element) for element in input().split()])

if orders_line:
    print(max(orders_line))

while orders_line:
    if orders_line[0] <= food_quantity:
        food_quantity -= orders_line[0]
        orders_line.popleft()
    else:
        break

if orders_line: # food was not enough, orders not fulfilled
    orders_line = collections.deque(map(str, orders_line))
    print(f'Orders left: {" ".join(orders_line)}')

else: # all orders served
    print("Orders complete")