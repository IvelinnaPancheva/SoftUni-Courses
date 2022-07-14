data = input()
countries_population = dict()
cities = dict()

while data != "report":
    # city|country|population
    split_data = data.split("|")
    city, country, population = split_data[0], split_data[1], int(split_data[2])

    if country not in countries_population:
        countries_population[country] = population
    else:
        countries_population[country] += population

    if country not in cities:
        cities[country] = {city: population}
    else: # country in cities
        cities[country][city] = population

    data = input()

sorted_by_population = dict(sorted(countries_population.items(), key=lambda x: -x[1]))

for country in sorted_by_population.keys():
    print(f"{country} (total population: {sorted_by_population[country]})")
    for key in cities.keys():
        if country == key:
            sorted_value = dict(sorted(cities[country].items(), key= lambda x: -x[1]))
            for city, population in sorted_value.items():
                print(f"=>{city}: {population}")