
class PlantError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class WaterError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class Plant:
    def __init__(self, name: str, water: int, sun: int):
        self.name = name
        self.water = water
        self.sun = sun


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []


class GardenManager:
    def add_plants_to_garden(plant: Plant, garden: Garden):
        try:
            if plant.name is None or plant.name == "":
                raise PlantError("")
            garden.plants.append(plant)
        except PlantError as e:
            print(e)

    def watering_plants(garden: Garden, water_range: int):
        try:
            for plant in garden.plants:
                if plant is None or water_range < 0:
                    raise WaterError("")
                else:
                    print("")
        except WaterError as e:
            print(e)
    
