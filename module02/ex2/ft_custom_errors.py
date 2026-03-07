class GardenError(Exception):
    """Base class for all custom garden-related exceptions."""
    def __init__(self, name: str) -> None:
        super().__init__(name)


class PlantError(GardenError):
    """Raised when a plant-related issue occurs (e.g., wilting)."""
    def __init__(self, name: str) -> None:
        super().__init__(name)


class WaterError(GardenError):
    """Raised when a watering-related issue occurs
      (e.g., insufficient water)."""
    def __init__(self, name: str) -> None:
        super().__init__(name)


def testing_plantError(name: str) -> None:
    """Raise and catch a PlantError, printing a descriptive message."""
    try:
        raise PlantError(f"The {name} plant is wilting!")
    except PlantError as e:
        print("Caught ", PlantError.__name__, e)


def testing_waterError() -> None:
    """Raise and catch a WaterError, printing a descriptive message."""
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print("Caught ", WaterError.__name__, e)


def testing_gardenError(name: str) -> None:
    """Demonstrate catching all garden-related errors via base class."""
    try:
        raise PlantError(f"The {name} plant is wilting!")
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print("Caught a garden error:", e)


def test_custom_errors() -> None:
    """Run tests for all custom garden error classes and print results."""
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    testing_plantError("tomato")
    print(end="\n")
    print("Testing WaterError...")
    testing_waterError()
    print(end="\n")
    print("Testing catching all garden errors...")
    testing_gardenError("tomato")
    print(end="\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
