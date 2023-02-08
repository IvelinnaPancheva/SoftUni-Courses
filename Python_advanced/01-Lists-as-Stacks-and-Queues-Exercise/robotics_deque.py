from collections import deque


def convert_time_to_seconds(string):
    time_data = string.split(':')
    hours, minutes, seconds = int(time_data[0]), int(time_data[1]), int(time_data[2])
    seconds = seconds + minutes * 60 + hours * 60 * 60
    full_day = 86400
    seconds %= full_day
    return seconds


def convert_sec_to_time(number):
    number %= 86400
    hours = number // 3600
    number -= hours * 3600
    minutes = number // 60
    number -= minutes * 60
    seconds = number
    time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return time


robots_speed = {}
product_queue = deque()
busy_until_time_sec = {}
robot_data = input().split(';')
for robot in robot_data:
    name, speed = robot.split('-')[0], int(robot.split('-')[1])
    robots_speed[name] = speed
    busy_until_time_sec[name] = -1
start_time_sec = convert_time_to_seconds(input())
product = input()
while not product == "End":
    product_queue.append(product)
    product = input()

begin_process_time = start_time_sec
while product_queue:
    begin_process_time += 1
    for robot, time in busy_until_time_sec.items():
        if time == -1 or time <= begin_process_time:
            busy_until_time_sec[robot] = begin_process_time + robots_speed[robot]
            print(f"{robot} - {product_queue.popleft()} [{convert_sec_to_time(begin_process_time)}]")
            break
    else:
        product_queue.rotate(-1)
