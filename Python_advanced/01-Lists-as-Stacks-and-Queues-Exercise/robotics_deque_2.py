from collections import deque


def convert_time_to_seconds(string):
    time_data = string.split(':')
    hours, minutes, seconds = int(time_data[0]), int(time_data[1]), int(time_data[2])
    seconds = seconds + minutes * 60 + hours * 60 * 60
    seconds %= 86400
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
first_free_second = {}

robot_data = input().split(';')
start_time_sec = convert_time_to_seconds(input())

for i in range(len(robot_data)):
    robot = robot_data[i]
    name, speed = robot.split('-')[0], int(robot.split('-')[1])
    robots_speed[name] = speed
    first_free_second[name] = start_time_sec + i

product = input()
while not product == "End":
    product_queue.append(product)
    product = input()

begin_process_time = start_time_sec
while product_queue:
    begin_process_time += 1
    for robot, time in first_free_second.items():
        if time <= begin_process_time:
            first_free_second[robot] = begin_process_time + robots_speed[robot]
            print(f"{robot} - {product_queue.popleft()} [{convert_sec_to_time(begin_process_time)}]")
            break
    else:
        product_queue.rotate(-1)
