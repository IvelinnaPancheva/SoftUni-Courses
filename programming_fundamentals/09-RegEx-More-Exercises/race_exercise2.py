import re

participants = input().split(", ")
data = input()

racer_pattern = r"[A-Za-z]"
digits_pattern = r"\d"
racers = {}

while data != "end of race":
    racer_name = re.findall(racer_pattern, data)
    racer = "".join(racer_name)
    digits_list = re.findall(digits_pattern, data)
    digits_list = list(map(int, digits_list))
    distance_km = sum(digits_list)

    if racer in participants:
        if racer not in racers:
            racers[racer] = distance_km
        else:
            racers[racer] += distance_km

    data = input()


racers = dict(sorted(racers.items(), key=lambda x: -x[1]))

while len(racers) > 3:
    racers.popitem()

top_three = []
for racer in racers:
    top_three.append(racer)

print(f"1st place: {top_three[0]}\n2nd place: {top_three[1]}\n3rd place: {top_three[2]}")
