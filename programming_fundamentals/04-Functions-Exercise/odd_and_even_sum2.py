def even_sum(integer_var):
    even_sum = []
    for element in str(integer_var):
        if int(element) % 2 == 0:
            even_sum.append(int(element))
    return sum(even_sum)


def odd_sum(integer_var):
    odd_sum = []
    for element in str(integer_var):
        if int(element) % 2 != 0:
            odd_sum.append(int(element))
    return sum(odd_sum)


number = int(input())
current_even_sum = even_sum(number)
current_odd_sum = odd_sum(number)
print(f"Odd sum = {current_odd_sum}, Even sum = {current_even_sum}")