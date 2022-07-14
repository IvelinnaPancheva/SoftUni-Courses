data = input()
cards_book = dict()
power_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
type_values = {"S": 4, "H": 3, "D": 2, "C": 1}
player_values = {}
while data != "JOKER":
    split_data = data.split(": ")
    name = split_data[0]
    cards = split_data[1].split(", ")
    cards = list(set(cards))
    if name not in cards_book:
        cards_book[name] = cards
    else:
        for card in cards:
            if card not in cards_book[name]:
                cards_book[name].append(card)
    data = input()

for player, cards in cards_book.items():
    total_value = 0
    for card in cards:
        current_power = card[:-1]
        current_type = card[-1]
        total_value += power_values[current_power] * type_values[current_type]
    player_values[player] = total_value

for player, value in player_values.items():
    print(f"{player}: {value}")