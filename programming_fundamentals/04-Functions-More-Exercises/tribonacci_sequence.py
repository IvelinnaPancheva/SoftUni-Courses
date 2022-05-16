def tribonacci_sequence(number):
    if 0 <= number <= 3:
        tribonacci_list = ['1', '1', '2']
        return " ".join(tribonacci_list[0:number])
    else: # number > 3
        tribonacci_list = [1, 1, 2]
        temp_list = tribonacci_list.copy()
        for x in range(4, number + 1):
            current_sum = sum(temp_list)
            tribonacci_list.append(current_sum)
            temp_list.append(current_sum)
            temp_list.pop(0)
        print_tribonacci = ""
        for element in tribonacci_list:
            print_tribonacci += str(element) + " "

        return print_tribonacci


current_number= int(input())
print(tribonacci_sequence(current_number))