class GardenError(Exception):
    def __init__(self, name: str):
        super().__init__(name)


class PlantError(GardenError):
    def __init__(self, name: str):
        super().__init__(name)


class WaterError(GardenError):
    def __init__(self, name):
        super().__init__(name)


def testing_plantError(name: str):
    try:
        raise PlantError(f"The {name} plant is wilting!")
    except PlantError as e:
        print("Caught ", PlantError.__name__, e)


def testing_waterError():
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print("Caught ", WaterError.__name__, e)


def testing_gardenError(name: str):
    try:
        raise PlantError(f"The {name} plant is wilting!")
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print("Caught a garden error:", e)


def test_all():
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
    test_all()
