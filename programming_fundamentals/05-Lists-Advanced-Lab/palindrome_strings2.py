sequence = input().split(" ")
palindrome = input()
palindrome_list = list()

for word in sequence:
    reversed_word = "".join(reversed(word))
    if reversed_word == word:
        palindrome_list.append(word)

count_palindrome = sequence.count(palindrome)
print(palindrome_list)
print(f"Found palindrome {count_palindrome} times")
