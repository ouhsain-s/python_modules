
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
    def __init__(self, owner, tank):
        self.owner = owner
        self.plants = []
        self.tank = tank


class GardenManager:
    def add_plant(plant: Plant, garden: Garden):
        try:
            if plant.name is None or plant.name == "":
                raise PlantError("Error adding plant: Plant name cannot be "
                                 "empty!")
            garden.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(e)

    def water_plants(cls, garden: Garden, water_range: int):
        print("Opening watering system")
        try:
            for plant in garden.plants:
                cls.check_tank(garden, water_range)
                if plant is None or water_range < 0:
                    raise WaterError("water NOT-valid plant!")
                else:
                    plant.water += water_range
                    garden.tank -= water_range
                    print(f"Watering {plant.name} - success")
        except WaterError as e:
            print(e)
        except GardenError as e:
            print(e, "\nSystem recovered and continuing...")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(water_level, sun_light):
        if water_level < 1:
            raise WaterError(f"Error checking lettuce: Water level "
                             f"{water_level} is too low (min 1)")
        if water_level > 10:
            raise WaterError(f"Error checking lettuce: Water level "
                             f"{water_level} is too high (max 10)")
        if sun_light < 2:
            raise WaterError(f"Error checking lettuce: sun "
                             f"{sun_light} is too low (min 2)")
        if sun_light > 12:
            raise WaterError(f"Error checking lettuce: sun "
                             f"{sun_light} is too high (max 12)")

    def check_plant_health(cls, garden: Garden):
        try:
            for plant in garden.plants:
                cls.check_health(plant.water, plant.sun)
                print(f"{plant.name}: healthy! (water: {plant.water}, sun:"
                      f" {plant.sun})")
        except GardenError as e:
            print(e)

    def check_tank(garden: Garden, water_requested):
        if garden.tank < water_requested:
            raise GardenError("Caught GardenError: Not enough water in tank")


def test_garden_management():
    bramz = Garden("Bramz", 12)
    tomato = Plant("tomato", 0, 8)
    lettuce = Plant("tettuce", 10, 8)
    empty = Plant("", 9, 9)
    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    GardenManager.add_plant(tomato, bramz)
    GardenManager.add_plant(lettuce, bramz)
    GardenManager.add_plant(empty, bramz)
    print(end="\n")
    print("Watering plants...")
    GardenManager.water_plants(GardenManager, bramz, 5)
    print(end="\n")
    print("Checking plant health...")
    GardenManager.check_plant_health(GardenManager, bramz)
    print("")
    print("Testing error recovery...")
    try:
        GardenManager.check_tank(bramz, 2)
    except GardenError as e:
        print(e, "\nSystem recovered and continuing...")
    print(end="\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
