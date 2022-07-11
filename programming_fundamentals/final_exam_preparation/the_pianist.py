n = int(input())

pieces = {}
for _ in range(n):
    # "{piece}|{composer}|{key}".
    data = input().split("|")
    piece, composer, key = data[0], data[1], data[2]
    if piece not in pieces:
        pieces[piece] = {"composer": composer, "key": key}

command = input()

while command != "Stop":
    split_data = command.split("|")
    # "Add|{piece}|{composer}|{key}":
    if split_data[0] == "Add":
        piece, composer, key = split_data[1], split_data[2], split_data[3]

        if piece not in pieces:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else: # piece is in collection pieces
            print(f"{piece} is already in the collection!")
    # "Remove|{piece}":
    elif split_data[0] == "Remove":
        piece = split_data[1]

        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")

        else: # piece is not in collection
            print(f"Invalid operation! {piece} does not exist in the collection.")

    # "ChangeKey|{piece}|{new key}":
    elif split_data[0] == "ChangeKey":
        piece = split_data[1]
        new_key = split_data[2]

        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

        else: # piece not in collection
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for piece in pieces:
    print(f"{piece} -> Composer: {pieces[piece]['composer']}, Key: {pieces[piece]['key']}")
