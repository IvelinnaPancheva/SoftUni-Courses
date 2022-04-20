start_num = int(input())
end_num = int(input())
magical_num = int(input())
magical_combination_found = False
combination_counter = 0

for x in range(start_num, end_num+1):
    for y in range(start_num, end_num + 1):
        combination_counter += 1
        if x + y == magical_num:
            magical_combination_found = True
            break
    if magical_combination_found:
        break

if magical_combination_found:
    print(f"Combination N:{combination_counter} ({x} + {y} = {magical_num})")
else:
    print(f"{combination_counter} combinations - neither equals {magical_num}")
