n = int(input())

durations = {}
addresses = {}

for i in range(n):
    log = input().split(" ")
    ipaddress, user, duration = log[0], log[1], int(log[2])
    if user not in durations:
        durations[user] = duration
    else:
        durations[user] += duration

    if user not in addresses:
        addresses[user] = [ipaddress]
    else:
        if ipaddress not in addresses[user]:
            addresses[user].append(ipaddress)

durations = dict(sorted(durations.items(), key= lambda x: x[0]))

for user, time in durations.items():
    for name, ip in addresses.items():
        if user == name:
            ip = list(sorted(ip))
            ip = ", ".join(ip)
            print(f"{name}: {time} [{ip}]")

