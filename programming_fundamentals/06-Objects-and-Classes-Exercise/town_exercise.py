class Town:
    def __init__(self, name:str, latitude: str = "0°N", longitude: str = "0°E"):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def set_latitude(self, new_latitude: str):
        self.latitude = new_latitude

    def set_longitude(self, new_longitude: str):
        self.longitude = new_longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)

town = Town("Ruse")
town.set_latitude("52° 41\' 91.04\" N")
town.set_longitude("33° 19\' 66.94\" E")
print(town)