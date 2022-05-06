n = int(input())

positive_list = list()
negative_list = list()
sum_of_negatives = 0
positive_count = 0

for i in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive_list.append(current_number)
        positive_count += 1
    else:
        negative_list.append(current_number)

print(positive_list)
print(negative_list)

for j in range(len(negative_list)):
    sum_of_negatives += negative_list[j]

print(f"Count of positives: {positive_count}")
print(f"Sum of negatives: {sum_of_negatives}")