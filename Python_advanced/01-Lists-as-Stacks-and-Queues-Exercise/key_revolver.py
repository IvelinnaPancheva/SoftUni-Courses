from collections import deque

bullet_price = int(input())
revolver_capacity = int(input()) # the amount of bullets per reloading
# to indicate when reloading if counter == barrel capacity
fire_counter = revolver_capacity
# while going through the bullets back-to-front - stack
bullets_stack = deque([int(element) for element in input().split()])
# starts to shoot the locks front-to-back - queue
locks_queue = deque([int(element) for element in input().split()])
intelligence_value = int(input())

while bullets_stack and locks_queue:
    right_bullet = bullets_stack[-1]
    first_lock = locks_queue[0]
    if right_bullet <= first_lock: # successful shot
        print("Bang!")
        locks_queue.popleft()

    else: # bullet > lock, failure
        print("Ping!")

    bullets_stack.pop()
    intelligence_value -= bullet_price
    fire_counter -= 1
    if bullets_stack and fire_counter == 0:
        print("Reloading!")
        fire_counter = revolver_capacity

if locks_queue: # mission failed
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")
else: # all locks were opened
    print(f"{len(bullets_stack)} bullets left. Earned ${intelligence_value}")
