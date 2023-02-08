from time import time
start = time()

bracket_stack = []
parentheses = input()
balance = True
for i in range(len(parentheses)):
    if parentheses[i] == "(" or parentheses[i] == "[" or parentheses[i] == "{":
        bracket_stack.append(parentheses[i])
    elif parentheses[i] == ")":
        if not bracket_stack:
            balance = False
            break
        if bracket_stack[-1] == "(":
            bracket_stack.pop()
    elif parentheses[i] == "]":
        if not bracket_stack:
            balance = False
            break
        if bracket_stack[-1] == "[":
            bracket_stack.pop()
    elif parentheses[i] == "}":
        if not bracket_stack:
            balance = False
            break
        if bracket_stack[-1] == "{":
            bracket_stack.pop()

if not bracket_stack and balance:
    print("YES")
else:
    print("NO")

print(f'Time taken to run: {time() - start} seconds')

