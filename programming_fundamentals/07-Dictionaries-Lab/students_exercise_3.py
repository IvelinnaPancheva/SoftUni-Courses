data = input()
courses = dict()

while ":" in data:
    student_name, id_num, course_name = data.split(":")

    if course_name not in courses:
        courses[course_name] = {}
    courses[course_name][id_num] = student_name

    data = input()

searched_course = data.split("_")
searched_course = " ".join(searched_course)

for course_name in courses.keys():
    if searched_course == course_name:
        for student in courses[course_name]:
            print(f"{courses[course_name][student]} - {student}")


