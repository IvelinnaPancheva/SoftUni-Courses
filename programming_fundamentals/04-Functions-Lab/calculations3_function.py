def calculator(operand, a, b):
    result = 0
    if operand == "multiply":
        result = a * b
    elif operand == "divide":
        result = a // b
    elif operand == "add":
        result = a + b
    elif operand == "subtract":
        result = a - b
    return result


operator = input()
x = int(input())
y = int(input())
print(calculator(operator, x, y))
