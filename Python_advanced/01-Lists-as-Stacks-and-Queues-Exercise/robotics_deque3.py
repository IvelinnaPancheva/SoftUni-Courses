from collections import deque


class Robot:
    def __init__(self, name, speed, start_time):
        self.name = name
        self.speed = speed
        self.start_time = start_time


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


product_queue = deque()
robot_data = input().split(';')
robots = []
for robot in robot_data:
    name, speed = robot.split('-')[0], int(robot.split('-')[1])
    current_robot = Robot(name, speed, -1)
    robots.append(current_robot)

start_time_sec = convert_time_to_seconds(input())
product = input()
while not product == "End":
    product_queue.append(product)
    product = input()

begin_process_time = start_time_sec
while product_queue:
    begin_process_time += 1
    for robot in robots:
        if robot.start_time == -1 or robot.start_time <= begin_process_time:
            robot.start_time = begin_process_time + robot.speed
            print(f"{robot.name} - {product_queue.popleft()} [{convert_sec_to_time(begin_process_time)}]")
            break
    else:
        product_queue.rotate(-1)
