class Zoo:
    __animals = 0  # private attribute

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, animal):
        Zoo.__animals += 1
        if species == "mammal":
            self.mammals.append(animal)
        elif species == "fish":
            self.fish.append(animal)
        elif species == "bird":
            self.birds.append(animal)

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fish)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


zoo_park = Zoo(input())
num_of_animals = int(input())
for animal in range(num_of_animals):
    animal_info = input().split(" ")
    animal_species = animal_info[0]
    animal_name = animal_info[1]
    zoo_park.add_animal(animal_species, animal_name)

species_to_print = input()
print(zoo_park.get_info(species_to_print))