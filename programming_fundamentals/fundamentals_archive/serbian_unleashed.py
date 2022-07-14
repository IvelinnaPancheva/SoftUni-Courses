import re
# validity_pattern = r"^(?P<singer>[A-Za-z]+ *[A-Za-z]* *[A-Za-z]*) @(?P<venue>[A-Za-z]+ *[A-Za-z]* *[A-Za-z]*) (?P<price>\d+) (?P<count>\d+)$"
validity_pattern = r"^(?P<singer>[A-Za-z]+ *[A-Za-z]* *[A-Za-z]*) @(?P<venue>[A-Za-z]+ *[A-Za-z]* *[A-Za-z]*) (?P<price>\d+) (?P<count>\d+)$"
venues = {}
data = input()
while data != "End":
    matches = re.finditer(validity_pattern, data)
    for match in matches:
        singer = match.group("singer")
        venue = match.group("venue")
        price = int(match.group("price"))
        count = int(match.group("count"))
        income = price * count
        if venue not in venues:
            venues[venue] = {singer: income}
        else: # venue is in dict
            if singer not in venues[venue]:
                venues[venue][singer] = income
            else: # singer is in the venue already
                venues[venue][singer] += income

    data = input()

for venue in venues:
    print(f"{venue}")
    singers = venues[venue]
    singers = dict(sorted(singers.items(), key=lambda x: -x[1]))
    for name, income in singers.items():
        print(f"#  {name} -> {income}")