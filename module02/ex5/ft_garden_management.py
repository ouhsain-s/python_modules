class GardenError(Exception):
    """Base class for garden-related custom exceptions."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Raised when a plant-related error occurs (e.g., invalid name)."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Raised when a watering-related error occurs (e.g., tank empty)."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Plant:
    """Represents a plant with name, water level, and sunlight exposure."""
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun


class Garden:
    """Represents a garden with an owner, plants list, and water tank."""
    def __init__(self, owner: str, tank: int) -> None:
        self.owner = owner
        self.plants = []
        self.tank = tank


class GardenManager:
    """Manages garden operations: adding, watering,
         and checking plant health."""
    def add_plant(plant: Plant, garden: Garden) -> None:
        """Add a plant to the garden, raising PlantError if name is invalid."""
        try:
            if plant.name is None or plant.name == "":
                raise PlantError("Error adding plant: Plant name cannot be "
                                 "empty!")
            garden.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(e)

    def water_plants(cls, garden: Garden, water_range: int) -> None:
        """Water all plants in the garden, handling errors and tank limits."""
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

    def check_health(water_level: int, sun_light: int) -> None:
        """Validate water and sunlight levels for a plant,
             raising errors if invalid."""
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

    def check_plant_health(cls, garden: Garden) -> None:
        """Check health of all plants in the garden,
             reporting errors if any."""
        for plant in garden.plants:
            cls.check_health(plant.water, plant.sun)
            print(f"{plant.name}: healthy! (water: {plant.water}, sun:"
                  f" {plant.sun})")

    def check_tank(garden: Garden, water_requested: int) -> None:
        """Ensure the garden tank has enough water for requested amount."""
        if garden.tank < water_requested:
            raise GardenError("Caught GardenError: Not enough water in tank")


def test_garden_management() -> None:
    """Run a full test of garden management:
         adding, watering, and health checks.
    Demonstrates error handling and system recovery."""
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
    try:
        GardenManager.check_plant_health(GardenManager, bramz)
    except GardenError as e:
        print(e)
    print(end="\n")
    print("Testing error recovery...")
    try:
        GardenManager.check_tank(bramz, 20)
        print("there is enough water in tank")
    except GardenError as e:
        print(e, "\nSystem recovered and continuing...")
    print(end="\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
