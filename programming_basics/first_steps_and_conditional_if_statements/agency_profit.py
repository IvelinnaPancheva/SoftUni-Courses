company = str(input())
adult_tickets = int(input())
children_tickets = int(input())
net_price_adult = float(input())
agency_margin = float(input())

price_adult = net_price_adult + agency_margin
price_children = (net_price_adult - 0.7 * net_price_adult) + agency_margin
profit = (price_adult * adult_tickets + price_children * children_tickets) * 0.2

print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")