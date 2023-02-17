n = int(input())
student_grades = dict()
for _ in range(n):
    student_name, grade = input().split()
    if student_name not in student_grades:
        student_grades[student_name] = []
    student_grades[student_name].append(float(grade))
for data in student_grades.items():
    average = sum(data[1]) / len(data[1])
    grades = [f"{x:.2f}" for x in data[1]]
    print(f"{data[0]} -> {' '.join(grades)} (avg: {average:.2f})")