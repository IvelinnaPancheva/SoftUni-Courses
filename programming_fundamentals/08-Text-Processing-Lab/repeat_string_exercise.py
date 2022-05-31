sequence = input().split(" ")
final_string = ""
for element in sequence:
    final_string += len(element) * element

print(final_string)
