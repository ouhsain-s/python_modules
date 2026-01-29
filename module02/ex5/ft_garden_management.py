
class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


class WaterError(GardenError):
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
        finally:
            print("")

    def check_plant_health(plant_name, water_level):
        if plant_name == "" or plant_name is None:
            raise PlantError("")
        if water_level < 1:
            raise WaterError(f"")
        if water_level > 10:
            raise WaterError(f"")

    def checking_health(cls, garden: Garden):
        try:
            for plant in garden.plants:
                cls.check_plant_health(plant.name, plant.wather, plant.sun)
            print("")
        except GardenError as e:
            print(e)
