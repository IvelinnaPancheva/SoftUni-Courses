def push(stack, num):
    stack.append(num)
    return stack


def pop(stack):
    if stack:
        stack.pop()
    return stack


def max_in_stack(stack):
    if stack:
        print(max(stack))


def min_in_stack(stack):
    if stack:
        print(min(stack))


def stack_from_top_to_bottom(stack):
    output = []
    for i in range(len(stack) - 1, -1, -1):
        output.append(str(stack.pop()))
    return output


numbers_stack = []
n = int(input())
for i in range(n):
    query = input().split()
    if query[0] == "1":
        current_number = int(query[1])
        numbers_stack = push(numbers_stack, current_number)

    elif query[0] == "2":
        numbers_stack = pop(numbers_stack)

    elif query[0] == "3":
        max_in_stack(numbers_stack)

    elif query[0] == "4":
        min_in_stack(numbers_stack)

print(", ".join(stack_from_top_to_bottom(numbers_stack)))
