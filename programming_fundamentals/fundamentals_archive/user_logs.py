data = input()

usernames = {}
while data != "end":
    # IP=(IP.Address) message=(A&sample&message) user=(username)
    split_data = data.split(" ")
    ip_address = (split_data[0].split("="))[1]
    user = (split_data[2].split("="))[1]
    if user not in usernames:
        usernames[user] = {ip_address: 1}
    else: # user is in usernames
        if ip_address not in usernames[user]:
            usernames[user][ip_address] = 1
        else: # user + ip address exist in usernames
            usernames[user][ip_address] += 1

    data = input()

sorted_users = dict(sorted(usernames.items(), key=lambda x: x[0]))

for user, log in sorted_users.items():
    output = []
    print(f"{user}:")
    counter = 1
    for ip, count in log.items():
        if counter == len(log):
            output.append(f"{ip} => {count}.")
        else:
            output.append(f"{ip} => {count},")
            counter += 1
    print(" ".join(output))