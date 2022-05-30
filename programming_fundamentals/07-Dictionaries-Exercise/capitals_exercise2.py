countries = input().split(", ")
capitals = input().split(", ")

capital_cities = {country:capital for (country, capital) in zip(countries, capitals)}
for country, capital in capital_cities.items():
    print(f"{country} -> {capital}")
