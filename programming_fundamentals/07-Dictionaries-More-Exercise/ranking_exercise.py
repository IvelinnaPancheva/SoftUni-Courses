data = input()

contests = {}

while data != "end of contests":
    # "{contest}:{password for contest}"
    contest, password = data.split(":")
    contests[contest] = password
    data = input()

submissions = {}
data = input()

while data != "end of submissions":
    #"{contest}=>{password}=>{username}=>{points}"
    current_contest, current_password, username, points = data.split("=>")
    points = int(points)

    if current_contest in contests and current_password == contests[current_contest]:
        if username not in submissions:
            submissions[username] = {current_contest : points}
        else: # submissions[username] is existing key, nested dict has contest + points stored
            if current_contest in submissions[username]:
               if points > submissions[username][current_contest]:
                   submissions[username][current_contest] = points

            else: # current contest is not a key in the nested dictionary
                submissions[username][current_contest] = points
    data = input()

max_points = 0
best_candidate = ""
total_points = 0
for student in submissions:
    for key in submissions[student]:
        total_points += submissions[student][key]
    if total_points > max_points:
        max_points = total_points
        best_candidate = student
    total_points = 0
print(f"Best candidate is {best_candidate} with total {max_points} points.")

sorted_submissions = sorted(submissions.items(), key=lambda x: x)
print("Ranking:")
for student in sorted_submissions:
    print((student[0]))
    sub_dict = student[1]
    sub_dict = sorted(sub_dict.items(), key=lambda x: -x[1])
    for element in sub_dict:
        print(f"#  {element[0]} -> {element[1]}")