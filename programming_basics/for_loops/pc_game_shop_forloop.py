games_sold = int(input()) # total games sold
hearthstone_sales = 0
fornite_sales = 0
overwatch_sales = 0
others = 0

for game in range(games_sold):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_sales += 1
    elif game_name == "Fornite":
        fornite_sales += 1
    elif game_name == "Overwatch":
        overwatch_sales += 1
    else:
        others += 1

hearthstone_sales = hearthstone_sales / games_sold * 100
fornite_sales = fornite_sales / games_sold * 100
overwatch_sales = overwatch_sales / games_sold * 100
others = others / games_sold * 100

print(f"Hearthstone - {hearthstone_sales:.2f}%")
print(f"Fornite - {fornite_sales:.2f}%")
print(f"Overwatch - {overwatch_sales:.2f}%")
print(f"Others - {others:.2f}%")
