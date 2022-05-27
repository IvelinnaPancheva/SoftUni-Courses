data = input().split(":")
courses = dict()

while len(data) != 1:
    student_name = data[0]
    id_num = int(data[1])
    course_name = data[2]
    if course_name not in courses:
        courses[course_name] = {id_num: student_name}
    else:
        courses[course_name][id_num] = student_name

    data = input().split(":")

searched_course = "".join(data)
searched_course = searched_course.split("_")
searched_course = " ".join(searched_course)

for course_name in courses.keys():
    if searched_course == course_name:
        for student in courses[course_name]:
            print(f"{courses[course_name][student]} - {student}")


