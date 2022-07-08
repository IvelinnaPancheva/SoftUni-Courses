import re

text = input()

place_pattern = r"(?P<separator>=|\/)(?P<destination>[A-Z][a-zA-Z]{2}[a-zA-Z]*)(\1)"

matches = re.finditer(place_pattern, text)

valid_destinations = []
for match in matches:
    destination = match.group("destination")
    valid_destinations.append(destination)

travel_points = 0
for place in valid_destinations:
    travel_points += len(place)

valid_destinations = ", ".join(valid_destinations)

print(f"Destinations: {valid_destinations}")
print(f"Travel Points: {travel_points}")