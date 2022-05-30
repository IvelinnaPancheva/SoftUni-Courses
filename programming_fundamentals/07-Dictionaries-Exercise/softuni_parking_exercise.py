n = int(input())
parking = {}

for _ in range(n):
    command = input().split(" ")
    if command [0] == "register":
        username, license = command[1], command[2]
        if username not in parking:
            parking[username] = license
            print(f"{username} registered {license} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[username]}")
    elif command[0] == "unregister":
        username = command[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for car in parking:
    print(f"{car} => {parking[car]}")