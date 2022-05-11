operator = input()
x = int(input())
y = int(input())
result = 0

if operator == "multiply":
    result = x * y
elif operator == "divide":
    result = x // y
elif operator == "add":
    result = x + y
elif operator == "subtract":
    result = x - y

print(result)
