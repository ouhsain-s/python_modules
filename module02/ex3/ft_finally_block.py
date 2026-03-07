def water_plants(plant_list: list) -> None:
    """Water each plant in the list, handling invalid entries safely.
    Ensures cleanup actions always run in the finally block."""
    is_valid = False
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise ValueError("Error: Cannot water None - invalid plant!")
            print(f"Watering {plant}")
        is_valid = True
    except ValueError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
        if is_valid:
            print("Watering completed successfully!")


def test_watering_system() -> None:
    """Run tests for the garden watering system with normal and error cases.
    Demonstrates that cleanup always executes."""
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print(end="\n")
    print("Testing with error...")
    plants[1] = ""
    water_plants(plants)
    print(end="\n")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
