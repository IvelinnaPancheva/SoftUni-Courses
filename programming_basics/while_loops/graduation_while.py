student = input()

good_grades_counter = 0
bad_grades_counter = 0
bad_grades_in_row_counter = 0
years_counter = 0
average_grade = 0
student_has_successful_graduation = True
average = 0

while good_grades_counter != 12 and bad_grades_in_row_counter < 2:
    current_grade = float(input())
    if current_grade >= 4:
        good_grades_counter += 1
        years_counter += 1
        bad_grades_in_row_counter = 0
        average_grade += current_grade

    else:  # current_grade < 4
        bad_grades_counter += 1
        bad_grades_in_row_counter += 1
        if bad_grades_in_row_counter == 2:
            student_has_successful_graduation = False
            break
        else:
            years_counter += 1

if student_has_successful_graduation:
    average_grade = average_grade / 12
    print(f"{student} graduated. Average grade: {average_grade:.2f}")

else:  # student_has_successful_graduation = False
    print(f"{student} has been excluded at {years_counter} grade")