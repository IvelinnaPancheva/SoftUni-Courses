def repeat_string(entry_string, counter):
    result = ""
    for i in range(counter):
        result += entry_string
    return result


input_string = input()
count = int(input())
print(repeat_string(input_string, count))