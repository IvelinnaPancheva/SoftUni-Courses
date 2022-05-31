data = input()

contests = {}
students = {}

while not data == "no more time":
    split_data = data.split(" -> ")
    # "{username} -> {contest} -> {points}"
    username, contest, points = split_data[0], split_data[1], int(split_data[2])

    if contest not in contests: # contest is not yet a key in the contests dict
        contests[contest] = {username: points}
    else: # contest is existing key with username and points
        if username in contests[contest].keys():
            if points > contests[contest][username]:
                contests[contest][username] = points

        else: # username is not a key of the nested dictionary
            contests[contest][username] = points

    if username not in students:
        students[username] = [contest, points]
    else:
        if contest in students[username]:
            index = students[username].index(contest)
            if points > students[username][index + 1]:
                students[username][index + 1] = points
        else:
            students[username].append(contest)
            students[username].append(points)

    data = input()

for student in students:
    students[student] = [x for x in students[student] if type(x) == int]
    students[student] = sum(students[student])

for contest in contests:
    print(f"{contest}: {len(contests[contest])} participants")
    sub_dict = contests[contest]
    sub_dict = sorted(sub_dict.items(), key=lambda x: (-x[1], x[0]))
    counter = 1
    for student in sub_dict:
        print(f"{counter}. {student[0]} <::> {student[1]}")
        counter += 1

print(f"Individual standings:")
counter = 1
sorted_students = sorted(students.items(), key=lambda x: (-x[1], x[0]))
for student in sorted_students:
    print(f"{counter}. {student[0]} -> {student[1]}")
    counter += 1


