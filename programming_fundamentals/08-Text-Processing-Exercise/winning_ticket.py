def ticket_status_check(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    else: # length == 20, valid ticket - no match, winning or jackpot
        winning_symbols = ["@", '#', '$', '^']
        left_half = ticket[0:10]
        right_half = ticket[10:]
        for symbol in winning_symbols:
            for length in range(10, 5, -1):
                winning_comination = length * symbol
                if winning_comination in left_half and winning_comination in right_half:
                    if length == 10:
                        return f'ticket "{ticket}" - {length}{symbol} Jackpot!'
                    return f'ticket "{ticket}" - {length}{symbol}'
        return f'ticket "{ticket}" - no match'


tickets = input().split(",")
tickets = [x.strip() for x in tickets]

for current_ticket in tickets:
    print(ticket_status_check(current_ticket))