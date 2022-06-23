first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())
hours = 0

while students_count > 0:
    students_count -= first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
    hours += 1
    if hours % 4 == 0:
        students_count += first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
    if students_count <= 0:
        break

print(f"Time needed: {hours}h.")

