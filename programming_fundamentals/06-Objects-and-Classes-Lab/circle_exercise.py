class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = Circle.__pi * self.diameter
        return f"{circumference:.2f}"

    def calculate_area(self):
        area = Circle.__pi *( (self.diameter / 2)**2)
        return f"{area:.2f}"

    def calculate_area_of_sector(self, angle):
        sector_area = (angle / 360) * Circle.__pi * (self.diameter / 2)**2
        return f"{sector_area:.2f}"


circle = Circle(10)
angle = 5

print(circle.calculate_circumference())
print(circle.calculate_area())
print(circle.calculate_area_of_sector(angle))
