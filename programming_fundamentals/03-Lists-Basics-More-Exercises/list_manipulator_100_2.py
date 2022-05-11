initial_list = input().split(" ")
command = input().split(" ")
initial_list = list(map(int, initial_list))

while True:
    sub_list = []
    even_list = []
    odd_list = []
    first_list = []
    last_list = []
    maximum = 0
    minimum = 0
    index = 0
    if "end" in command[0]:
        break
    if command[0] == "exchange":
        current = int(command[1])
        if 0 <= current <= len(initial_list) - 1:
            sub_list = initial_list[0:current + 1]
            for i in range(current, -1, -1):
                initial_list.remove(initial_list[i])
            initial_list.extend(sub_list)
        else:
            print("Invalid index")

    if command[0] == "max":
        even_list = [i for i in initial_list if i % 2 == 0]
        odd_list = [i for i in initial_list if i % 2 != 0]

        if command[1] == "even":
            if len(even_list) == 0:
                print("No matches")
            else:
                maximum = max(even_list)
                for i in range(len(initial_list)):
                    if initial_list[i] == maximum:
                        index = i
                print(index)

        elif command[1] == "odd":
            if len(odd_list) == 0:
                print("No matches")
            else:
                maximum = max(odd_list)
                for i in range(len(initial_list)):
                    if initial_list[i] == maximum:
                        index = i
                print(index)

    if command[0] == "min":
        even_list = [i for i in initial_list if i % 2 == 0]
        odd_list = [i for i in initial_list if i % 2 != 0]

        if command[1] == "even":
            if len(even_list) == 0:
                print("No matches")
            else:
                minimum = min(even_list)
                for i in range(len(initial_list)):
                    if initial_list[i] == minimum:
                        index = i
                print(index)

        elif command[1] == "odd":
            if len(odd_list) == 0:
                print("No matches")
            else:
                minimum = min(odd_list)
                for i in range(len(initial_list)):
                    if initial_list[i] == minimum:
                        index = i
                print(index)

    if command[0] == "first":
        current = int(command[1])
        if current > len(initial_list):
            print("Invalid count")
        else:
            if command[2] == "even":
                even_list = [i for i in initial_list if i % 2 == 0]
                if current <= len(even_list):
                    for i in range(current):
                        first_list.append(even_list[i])
                else:
                    for i in range(len(even_list)):
                        first_list.append(even_list[i])
                print(first_list)

            if command[2] == "odd":
                odd_list = [i for i in initial_list if i % 2 != 0]
                if current <= len(odd_list):
                    for i in range(current):
                        first_list.append(odd_list[i])
                else:
                    for i in range(len(odd_list)):
                        first_list.append(odd_list[i])
                print(first_list)

    if command[0] == "last":
        current = int(command[1])
        if current > len(initial_list):
            print("Invalid count")
        else:
            if command[2] == "even":
                even_list = [i for i in initial_list if i % 2 == 0]
                if current < len(even_list):
                    while current < len(even_list):
                        even_list.pop(0)
                    print(even_list)
                else:
                    print(even_list)

            if command[2] == "odd":
                odd_list = [i for i in initial_list if i % 2 != 0]
                if current < len(odd_list):
                    odd_list = odd_list[-current:]
                    while current < len(odd_list):
                        odd_list.pop(0)
                    print(odd_list)
                else:
                    print(odd_list)

    command = input().split(" ")

print(initial_list)

