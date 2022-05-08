offerings_string = input().split(", ")
beggars = int(input())
integer_offerings = offerings_string.copy()
final_sum_list = []
temporary_sum = 0
counter_of_index = 0 # [0, beggars - 1] = num of beggars

for i in range(len(integer_offerings)):
    integer_offerings[i] = int(integer_offerings[i])

for i in range(counter_of_index, beggars):
    for offering in range(counter_of_index, len(integer_offerings), beggars):
        temporary_sum += integer_offerings[offering]

    final_sum_list.append(temporary_sum)
    temporary_sum = 0
    counter_of_index += 1

print(final_sum_list)