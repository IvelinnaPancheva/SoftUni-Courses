n_people = int(input())
p_capacity = int(input())

course_counter = 0

while n_people >= p_capacity:
    course_counter += n_people // p_capacity
    n_people %= p_capacity

if 0 < n_people < p_capacity:
    course_counter +=1

print(course_counter)