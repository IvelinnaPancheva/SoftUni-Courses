def calculator(operand, a, b):
    if operand == "multiply":
        return a * b
    elif operand == "divide":
        return a // b
    elif operand == "add":
        return a + b
    elif operand == "subtract":
        return a - b


operator = input()
x = int(input())
y = int(input())
result = calculator(operator, x, y)
print(result)
