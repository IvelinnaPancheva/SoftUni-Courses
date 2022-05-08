deck_list = input().split(" ")
count = int(input())
sublist1 = []
sublist2 = []
temporary_list = []

for i in range(count):
    for i in range(int(len(deck_list)/2)):
        sublist1.append(deck_list[i])
    for i in range(int(len(deck_list)/2), len(deck_list)):
        sublist2.append(deck_list[i])
    for i in range(len(sublist1)):
        temporary_list.append(sublist1[i])
        temporary_list.append(sublist2[i])
    deck_list = temporary_list.copy()
    temporary_list=[]
    sublist1 = []
    sublist2 = []

print(deck_list)
