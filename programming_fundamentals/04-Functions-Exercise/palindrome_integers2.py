def is_palindrome_check(list_variable):
    sequence_of_reversed = []
    for item in list_variable:
        current = ""
        for i in range(len(item)-1, -1, -1):
            current += item[i]
        sequence_of_reversed.append(current)

    for index in range(len(list_variable)):
        if list_variable[index] == sequence_of_reversed[index]:
            print("True")
        else:
            print("False")


num_sequence = input().split(", ")
is_palindrome_check(num_sequence)