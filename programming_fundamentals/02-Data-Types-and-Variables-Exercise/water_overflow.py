n = int(input())
capacity = 255
total_liters = 0

for i in range(n):
    liters = int(input())
    if total_liters + liters <= capacity:
        total_liters += liters
    else:
        print("Insufficient capacity!")

print(total_liters)