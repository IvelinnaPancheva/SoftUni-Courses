def tribonacci_sequence(number):
        print_tribonacci = ""
        tribonacci_list = []
        for x in range(1, number + 1):
            if x == 1 or x == 2:
                current = 1
                tribonacci_list.append(current)
            elif x == 3:
                current = sum(tribonacci_list)
                tribonacci_list.append(current)
            else:
                current = tribonacci_list[x-2] + tribonacci_list[x-3] + tribonacci_list[x-4]
                tribonacci_list.append(current)
        for element in tribonacci_list:
            print_tribonacci += str(element) + " "

        return print_tribonacci


current_number= int(input())
print(tribonacci_sequence(current_number))