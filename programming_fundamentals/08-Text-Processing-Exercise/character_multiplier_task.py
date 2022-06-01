data = input().split(" ")
first = data[0]
second = data[1]
total_sum = 0
if len(first) == len(second):
    for index in range(len(first)):
        total_sum += ord(first[index]) * ord(second[index])
elif len(first) > len(second):
    for index in range(len(second)):
        total_sum += ord(first[index]) * ord(second[index])
    for ind in range(index+1, len(first)):
        total_sum += ord(first[ind])
else:  # len(first)< len(second)
    for index in range(len(first)):
        total_sum += ord(first[index]) * ord(second[index])
    for ind in range(index+1, len(second)):
        total_sum += ord(second[ind])
print(total_sum)
