class Party:

    def __init__(self):
        self.people = []


current_party = Party()
while True:
    command = input()
    if command == "End":
        break
    current_party.people.append(command)

print(f"Going: {', '.join(current_party.people)}")
print(f"Total: {len(current_party.people)}")
