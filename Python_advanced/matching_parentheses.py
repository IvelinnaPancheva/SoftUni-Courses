expression = input()

# create a stack to keep track of the indices of each opening bracket ( and remove the
# opening bracket at the last index from the stack when the loop reaches a closing bracket )

parenthesis_stack = []
for index in range(len(expression)):
    if expression[index] == "(":
        parenthesis_stack.append(index)
    elif expression[index] == ")":
        start_index = parenthesis_stack.pop()
        print(expression[start_index:index+1])

