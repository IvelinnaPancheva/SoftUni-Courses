countries = input().split(", ")
capitals = input().split(", ")

capital_cities = {country:capital for (country, capital) in zip(countries, capitals)}
cities_to_print = [(print(f"{country} -> {capital}")) for (country, capital) in capital_cities.items()]