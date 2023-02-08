from collections import deque

green_light = int(input()) # During the green light, cars will enter and exit the crossroads one by one
free_window = int(input()) # During the free window, cars will only exit the crossroads

crossroad_deque = deque() # if empty after window - smooth pass, else - crash
total_cars_passed = deque() # successfully passed cars
lane = deque() # all cars, lined up at traffic light
crash = False # true if crossroad not empty after free window

command = input()
while not command == "END" and not crash:
    if command == "green":
        timer = green_light
        while lane and timer > 0:
            timer -= len(lane[0])
            crossroad_deque.append(lane.popleft())
        timer = green_light + free_window
        while crossroad_deque and timer > 0:
            if timer - len(crossroad_deque[0]) >= 0:
                timer -= len(crossroad_deque[0])
                total_cars_passed.append(crossroad_deque.popleft())
            else: # timer - len(crossroad_deque[0]) < 0
                crash = True
                character = crossroad_deque[0][timer]
                print("A crash happened!")
                print(f"{crossroad_deque[0]} was hit at {character}.")
                break
    else: # if command == car brand
        lane.append(command)

    command = input()

if not crash: # if not crash
    print("Everyone is safe.")
    print(f"{len(total_cars_passed)} total cars passed the crossroads.")


