rooms = int(input())
free_chairs = 0
total_chairs = 0
total_visitors = 0

for room in range(1, rooms + 1):
    room_chairs = input().split(" ")
    chairs = len(room_chairs[0])
    total_chairs += chairs
    visitors = int(room_chairs[1])
    total_visitors += visitors

    if chairs >= visitors:
        free_chairs += chairs - visitors
    elif chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {room}")

if total_chairs >= total_visitors:
    print(f"Game On, {free_chairs} free chairs left")