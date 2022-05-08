carddeck_list = input().split(" ")
count = int(input())
left_list = []
right_list = []
temporary_list = []

for i in range(count):
    left_list = carddeck_list[0:len(carddeck_list)//2]
    right_list = carddeck_list[len(carddeck_list)//2::]
    for i in range(len(left_list)):
        temporary_list.append(left_list[i])
        temporary_list.append(right_list[i])
    carddeck_list = temporary_list
    temporary_list=[]

print(carddeck_list)
