def update_student_points(student_name, current_points, results_dict):
    if student_name not in results_dict or current_points > results_dict[student_name]:  # if false - username exists, student has submissions
        results_dict[student_name] = current_points
    return results_dict


def update_submissions_count(current_language, submissions_dict):
    if current_language not in submissions_dict:  # non existing key language in submissions
        submissions[current_language] = 1
    else:  # existing key language in submissions
        submissions_dict[current_language] += 1
    return submissions_dict


data = input()

results = {} # key = student username, value max points
submissions = {}  # key = programming language, value - count of submissions

while data != "exam finished":
    split_data = data.split("-")
    if "banned" not in split_data:
        username, language, points = split_data[0], split_data[1], int(split_data[2])
        results = update_student_points(username, points, results)
        submissions = update_submissions_count(language, submissions)

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
