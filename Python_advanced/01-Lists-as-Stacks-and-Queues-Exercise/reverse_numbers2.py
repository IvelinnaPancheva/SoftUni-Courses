numbers_stack = [int(element) for element in input().split()]
while numbers_stack:
    print(numbers_stack.pop(), end=" ")
