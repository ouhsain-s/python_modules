

class Plant:
    num_planst = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age
        print(f"Created: {self.name} ({self.height}cm, {self._age} days)")
        Plant.num_planst += 1


if __name__ == "__main__":

    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    print(f"\nTotal plants created: {Plant.num_planst}")
