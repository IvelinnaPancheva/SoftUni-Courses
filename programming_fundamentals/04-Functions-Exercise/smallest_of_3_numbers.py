def smallest_of_3_numbers(a, b, c):
    nums_list = [a, b, c]
    return min(nums_list)


first_num = int(input())
second_num = int(input())
third_num = int(input())
min_num = smallest_of_3_numbers(first_num, second_num, third_num)
print(min_num)