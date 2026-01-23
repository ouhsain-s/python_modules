class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.age = age
        self.height = height


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = diameter
        print(f"{name} (Tree): {height}cm, {age} days, {diameter}cm diameter")

    def produce_shade(self) -> None:
        shade_area = int(0.1 * self.height + 0.56 * self.trunk_diameter)
        print(f"{self.name} provides {shade_area} square meters of shade")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        print(f"{name} (Flower): {height}cm, {age} days, {color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, season: str) -> None:
        super().__init__(name, height, age)
        self.season = season
        print(f"{name} (Vegetable): {height}cm, {age} days, {season} harvest")

    def show_nutrition(self) -> None:
        value: str
        if self.season == "summer":
            value = "vitamin C"
        elif self.season == "fall":
            value = "vitamin A"
        elif self.season == "winter":
            value = "vitamin D"
        elif self.season == "spring":
            value = "vitamin E"
        else:
            value = "vitamin C"

        print(f"{self.name} is rich in {value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()
    print(end="\n")
    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    print(end="\n")
    tomato = Vegetable("Tomato", 80, 90, "summer")
    tomato.show_nutrition()
