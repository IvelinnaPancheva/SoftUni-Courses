def define_product_sign(x, y, z):
    num_list = [x, y, z]
    zero_is_in_list = False
    count_negative = 0
    for i in range(len(num_list)):
        if num_list[i] < 0:
            count_negative += 1
        if num_list[i] == 0:
            zero_is_in_list = True
    if zero_is_in_list:
        return "zero"
    elif count_negative % 2 == 0:
        return "positive"
    else:
        return "negative"


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(define_product_sign(first_num, second_num, third_num))
