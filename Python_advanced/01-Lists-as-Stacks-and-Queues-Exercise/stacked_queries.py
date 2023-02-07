numbers_stack = []
n = int(input())
for i in range(n):
    query = input().split()
    if query[0] == "1":
        current_number = int(query[1])
        numbers_stack.append(current_number)

    elif query[0] == "2":
        if numbers_stack:
            numbers_stack.pop()

    elif query[0] == "3":
        if numbers_stack:
            print(max(numbers_stack))

    elif query[0] == "4":
        if numbers_stack:
            print(min(numbers_stack))
output = []
for i in range(len(numbers_stack)-1, -1, -1):
    output.append(str(numbers_stack.pop()))
print(", ".join(output))
