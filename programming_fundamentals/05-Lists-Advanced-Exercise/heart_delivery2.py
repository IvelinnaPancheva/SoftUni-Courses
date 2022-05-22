houses = input().split("@") # houses even int hearts become a list of string values
houses = list(map(int, houses)) # even nums from string become int
command = input().split(" ") # command becomes a list with space for a separator
starting_index = 0

while command[0] != "Love!":
    current_length = int(command[1])  # value of jump
    if starting_index + current_length <= len(houses) - 1: # check if new index value is valid
        house_index = starting_index + current_length
        hearts = houses[house_index]
        if hearts == 0:
            print(f"Place {house_index} already had Valentine's day.")
        elif hearts >= 2:
            hearts -= 2
            houses[house_index] = hearts
            if hearts == 0:
                print(f"Place {house_index} has Valentine's day.")
        starting_index = house_index
    else: # starting index + current length > last index
        house_index = 0
        starting_index = 0
        hearts = houses[house_index]
        if hearts == 0:
            print(f"Place {house_index} already had Valentine's day.")
        elif hearts >= 2:
            hearts -= 2
            houses[house_index] = hearts
            if hearts == 0:
                print(f"Place {house_index} has Valentine's day.")

    command = input().split(" ")

print(f"Cupid's last position was {house_index}.")
if len(houses) == houses.count(0):
    print("Mission was successful.")
else:
    failed_houses = len(houses) - houses.count(0)
    print(f"Cupid has failed {failed_houses} places.")