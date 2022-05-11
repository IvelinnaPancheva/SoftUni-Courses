numbers_list = input().split(" ")
step = int(input())
removed = []
counter = 0

while len(removed) < len(numbers_list):
    for index in range(len(numbers_list)):
        if numbers_list[index] != "*":
            counter += 1
        if counter == step and numbers_list[index] != "*":
            removed.append(numbers_list[index])
            counter = 0
            numbers_list[index] = "*"

removed = ",".join(removed)
print(f"[{removed}]")

