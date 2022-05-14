def is_palindrome_check(string_variable):
        current = ""
        for i in range(len(string_variable)-1, -1, -1):
            current += string_variable[i]
        if string_variable == current:
            return "True"
        else:
            return "False"


num_sequence = input().split(", ")
for item in num_sequence:
    print(is_palindrome_check(item))