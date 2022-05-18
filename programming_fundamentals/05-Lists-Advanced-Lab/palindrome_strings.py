sequence = input().split(" ")
palindrome = input()

palindrome_list = [word for word in sequence if word == "".join(reversed(word))]
count_palindrome = sequence.count(palindrome)
print(palindrome_list)
print(f"Found palindrome {count_palindrome} times")
