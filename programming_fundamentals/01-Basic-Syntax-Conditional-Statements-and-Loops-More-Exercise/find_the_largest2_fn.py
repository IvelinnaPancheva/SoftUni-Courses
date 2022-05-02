def find_the_largest(text):
    var = list(text)
    var.sort(reverse=True)
    text = ''.join(var)
    return text


current_text = input()
print(find_the_largest(current_text))

