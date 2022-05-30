data = input()

results = {} # key = student username, value max points
submissions = {}  # key = programming language, value - count of submissions

while data != "exam finished":
    split_data = data.split("-")
    if "banned" not in split_data:
        username, language, points = split_data[0], split_data[1], int(split_data[2])
        if username not in results or points > results[username]:  # if false - username exists, student has submissions
            results[username] = points

        if language not in submissions:  # non existing key language in submissions
            submissions[language] = 1
        else:  # existing key language in submissions
            submissions[language] += 1

    else: # banned student, username must be deleted, but submissions kept
        username = split_data[0]
        if username in results:
            del results[username]

    data = input()

print("Results:")
for student, points in results.items():
    print(f"{student} | {points}")

print("Submissions:")
for language,counter in submissions.items():
    print(f"{language} - {counter}")
