def repeat_string(entry_string, counter):
    result = entry_string * counter
    return result


input_string = input()
count = int(input())
print(repeat_string(input_string, count))