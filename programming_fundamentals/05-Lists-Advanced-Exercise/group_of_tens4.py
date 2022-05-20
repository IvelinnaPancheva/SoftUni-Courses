def group_sorting_to_list(numbers):
    for index in range(len(numbers)):
        if numbers[index] <= ten_variable:
            current = numbers[index]
            output_list.append(current)
    return output_list


numbers_sequence = [int(x) for x in input().split(", ")]
ten_variable = 10

while len(numbers_sequence) > 0:
    output_list = []
    group_sorting_to_list(numbers_sequence)
    numbers_sequence = list(filter(lambda x: x if x not in output_list else not x, numbers_sequence))
    print(f"Group of {ten_variable}'s: {output_list}")
    ten_variable += 10