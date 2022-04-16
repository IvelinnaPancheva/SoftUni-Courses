result = 0

while result >= 0:
    current_number = float(input())
    if current_number < 0:
        print("Negative number!")
        break
    else: # current num > 0
        result = current_number * 2
        print(f"Result: {result:.2f}")