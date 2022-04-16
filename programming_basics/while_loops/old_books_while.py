favourite_book = input()

book_counter = 0
is_favourite_book_found = False
current_book = input()

while current_book != "No More Books":
    if current_book != favourite_book:
        book_counter += 1
        current_book = input()

    else: # current_book == favourite_book
        is_favourite_book_found = True
        print(f"You checked {book_counter} books and found it.")
        break

if is_favourite_book_found == False:
    print(f"The book you search is not here!")
    print(f"You checked {book_counter} books.")