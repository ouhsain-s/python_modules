class SecurePlant:

    def __init__(self, name: str) -> None:
        self.name = name
        self.height: int
        self.age: int
        print(f"Plant created: {name}")

    def set_height(self, height: str) -> None:
        if (height >= 0 & height <= 40000):
            self.height = height
            print(f"height updated: {height} days [OK]")
        else:
            print(f"Invalid operation attempted: height {height} [REJECTED]")
            if (height < 0):
                print("Security: Negative height rejected")

    def get_height(self):
        return self.height

    def set_age(self, age: str) -> None:
        if age >= 0:
            self.age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: Age {age} [REJECTED]")
            print("Security: Negative Aje rejected")

    def get_age(self):
        return self.age

    def get_info(self):
        return (f"Current plant: {self.name} ({self.height}, {self.age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(rose.get_info())
