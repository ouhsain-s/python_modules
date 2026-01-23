class Plant:
    def __init__(self) -> None:
        self.name: str
        self.height: int
        self._age: int

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self._age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self._age} days old"


if __name__ == "__main__":
    """Main program starts here"""

    rose = Plant()
    rose.name = "Rose"
    rose._age = 30
    rose.height = 25
    old_height = rose.height
    print("=== Day 1 ===")
    print(rose.get_info())
    for i in range(6):
        rose.grow()
        rose.age()
    print("=== Day 7 ===")
    print(rose.get_info())
    growth = rose.height - old_height
    print(f"Growth this week: +{growth}cm")
