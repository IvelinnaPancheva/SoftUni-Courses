bracket_stack = []
parentheses = input()
balance = True
for i in range(len(parentheses)):
    if parentheses[i] == "(" or parentheses[i] == "[" or parentheses[i] == "{":
        bracket_stack.append(parentheses[i])
    elif parentheses[i] in ")]}":
        if not bracket_stack:
            balance = False
            break
        elif bracket_stack[-1] + parentheses[i] in '()[]{}':
            bracket_stack.pop()
        elif bracket_stack[-1] + parentheses[i] not in '()[]{}':
            balance = False
            break

if not bracket_stack and balance:
    print("YES")
else:
    print("NO")