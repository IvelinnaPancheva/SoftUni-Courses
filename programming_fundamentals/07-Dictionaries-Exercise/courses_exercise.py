data = input()
courses = dict()

while data != "end":
    split_data = data.split(" : ")
    course_name, student = split_data[0], split_data[1]
    if course_name not in courses:
        courses[course_name] = [student]
    else:
        courses[course_name].append(student)

    data = input()

for course, students in courses.items():
    print(f"{course}: {len(courses[course])}")
    [print(f"-- {student_name}") for student_name in students]


