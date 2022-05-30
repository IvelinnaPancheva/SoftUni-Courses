n = int(input())
student_grades = {}

for _ in range(n):
    student = input()
    grade = float(input())
    if student not in student_grades:
        student_grades[student] = [grade]
    else:
        student_grades[student].append(grade)

filtered_dictionary = {}
for student in student_grades:
    average = sum(student_grades[student]) / len(student_grades[student])
    if average >= 4.5:
        filtered_dictionary[student] = average

for student in filtered_dictionary:
    print(f"{student} -> {filtered_dictionary[student]:.2f}")