text_as_stack = list(input())

for index in range(len(text_as_stack) - 1, -1, -1):
    print(text_as_stack.pop(), end="")
