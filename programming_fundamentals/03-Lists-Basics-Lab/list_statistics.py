n = int(input())
positive_list = list()
negative_list = list()
sum_of_negatives = 0

for i in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive_list.append(current_number)
    else:
        negative_list.append(current_number)
        sum_of_negatives += current_number

print(positive_list)
print(negative_list)

positive_count = len(positive_list)
print(f"Count of positives: {positive_count}")
print(f"Sum of negatives: {sum_of_negatives}")