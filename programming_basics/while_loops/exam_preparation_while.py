bad_grades_failure = int(input())

average_score = 0
number_problems = 0
sum_of_grades = 0
bad_grades_counter = 0
last_problem = ""
is_exam_successful = True

current_problem = input()

while current_problem != "Enough":
    current_score = int(input())
    number_problems += 1
    sum_of_grades += current_score
    last_problem = current_problem
    if current_score <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == bad_grades_failure:
            is_exam_successful = False
            print(f"You need a break, {bad_grades_counter} poor grades.")
            break
    current_problem = input()

average_score = sum_of_grades / number_problems

if is_exam_successful:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_problems}")
    print(f"Last problem: {last_problem}")

#  На първи ред - брой незадоволителни оценки - цяло число;
# •	След това многократно се четат по два реда:
# o	Име на задача – текст;
# o	Оценка - цяло число в интервала [2…6]