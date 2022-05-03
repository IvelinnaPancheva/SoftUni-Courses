from math import ceil

n_people = int(input())
p_capacity = int(input())

course_counter = ceil(n_people / p_capacity)

print(course_counter)