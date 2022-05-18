def sort_names_by_descending_len(names):
    sorted_names = sorted(names, key=lambda x: (-len(x), x))
    return  sorted_names


current_names = input().split(", ")
print(sort_names_by_descending_len(current_names))