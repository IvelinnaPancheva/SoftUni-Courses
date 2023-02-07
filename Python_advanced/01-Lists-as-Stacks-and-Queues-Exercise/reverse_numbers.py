numbers_stack = [int(element) for element in input().split()]
for i in range(len(numbers_stack)-1, -1, -1):
    print(numbers_stack.pop(), end=" ")
