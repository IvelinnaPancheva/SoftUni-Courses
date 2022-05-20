numbers = [int(x) for x in input().split(", ")]
ten_variable = 10

while len(numbers) > 0:
    output_list = []
    for index in range(len(numbers)):
        if numbers[index] <= ten_variable:
            current = numbers[index]
            output_list.append(current)
    for index in range(len(numbers)-1, -1, -1):
        if numbers[index] in output_list:
            numbers.pop(index)
    print(f"Group of {ten_variable}'s: {output_list}")
    ten_variable += 10