def group_sorting_to_list(numbers):
    for index in range(len(numbers)):
        if numbers[index] <= ten_variable:
            current = numbers[index]
            output_list.append(current)
    return output_list


def filtering_of_input(numbers):
    for index in range(len(numbers) - 1, -1, -1):
        if numbers[index] in output_list:
            numbers.pop(index)
    return numbers


numbers_sequence = [int(x) for x in input().split(", ")]
ten_variable = 10

while len(numbers_sequence) > 0:
    output_list = []
    group_sorting_to_list(numbers_sequence)

    filtering_of_input(numbers_sequence)

    print(f"Group of {ten_variable}'s: {output_list}")
    ten_variable += 10