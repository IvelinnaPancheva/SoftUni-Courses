def list_even_numbers(numbers_list):
    even_list = []
    for index in range(len(numbers_list)):
        if int(numbers_list[index]) % 2 == 0:
            even_list.append(int(numbers_list[index]))
    return even_list


num_sequence = input().split(" ")
print(list_even_numbers(num_sequence))