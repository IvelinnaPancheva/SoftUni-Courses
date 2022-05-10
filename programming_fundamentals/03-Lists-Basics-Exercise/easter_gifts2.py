gift_names = input()

gift_list = gift_names.split()

command = input()
while command != "No Money":
    command_list = command.split()

    if "OutOfStock" in command_list:
        for i in range(len(gift_list)):
            if gift_list[i] == command_list[-1]:
                gift_list[i] = "None"
    if "Required" in command_list:
        for i in range(len(gift_list)):
            if i == int(command_list[-1]):
                gift_list[i] = command_list[-2]
    if "JustInCase" in command_list:
        gift_list[-1] = command_list[-1]

    command = input()

for j in range(len(gift_list)-1, -1, -1):
    if "None" in gift_list[j]:
        gift_list.remove(gift_list[j])

final_gifts = " ".join(gift_list)
print(final_gifts)