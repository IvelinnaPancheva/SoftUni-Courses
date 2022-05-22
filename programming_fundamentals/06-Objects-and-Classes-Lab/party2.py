class Party:

    def __init__(self):
        self.people = []


current_party = Party()
command = input()
while command != "End":
    current_party.people.append(command)
    command = input()

print(f"Going: {', '.join(current_party.people)}")
print(f"Total: {len(current_party.people)}")
