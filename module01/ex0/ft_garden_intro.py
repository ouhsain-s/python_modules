def print_garden_intro(plant: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    name = "Rose"
    height = 25
    age = 30
    print_garden_intro("Rose", 25, 30)
