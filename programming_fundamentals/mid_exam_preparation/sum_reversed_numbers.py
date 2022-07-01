numbers = input().split(" ")
sum_of_reversed = 0

for element in numbers:
    temporary = "".join(reversed(element))
    temporary = int(temporary)
    sum_of_reversed += temporary

print(sum_of_reversed)
