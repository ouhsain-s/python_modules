def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    try:
        if plant_name == "" or plant_name is None:
            raise ValueError("Plant name cannot be empty!")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} "
                             "is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level}"
                             " is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             " is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             " is too high (max 12)")
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print("Error:", e)


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    plant_name = "tomato"
    water_level = 5
    sunlight_hours = 5
    check_plant_health(plant_name, water_level, sunlight_hours)
    print(end="\n")
    print("Testing empty plant name...")
    plant_name = ""
    water_level = 6
    sunlight_hours = 6
    check_plant_health(plant_name, water_level, sunlight_hours)
    print(end="\n")
    print("Testing bad water level...")
    plant_name = "tomato"
    water_level = 15
    sunlight_hours = 8
    check_plant_health(plant_name, water_level, sunlight_hours)
    print(end="\n")
    print("Testing bad sunlight hours...")
    plant_name = "tomato"
    water_level = 4
    sunlight_hours = 0
    check_plant_health(plant_name, water_level, sunlight_hours)
    print(end="\n")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
