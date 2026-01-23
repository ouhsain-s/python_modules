class SecurePlant:

    def __init__(self, name: str) -> None:
        self.name = name
        self.height: int
        self.age: int
        print(f"Plant created: {name}")

    def set_height(self, height: int) -> None:
        if (height >= 0):
            self.height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            if (height < 0):
                print("Security: Negative height rejected")

    def get_height(self) -> int:
        return self.height

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: Age {age} [REJECTED]")
            print("Security: Negative Age rejected")

    def get_age(self) -> int:
        return self.age

    def get_info(self) -> str:
        return (f"Current plant: {self.name} ({self.height}cm"
                f", {self.age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    print(end="\n")
    rose.set_height(-5)
    print(end="\n")
    print(rose.get_info())
