class Planst:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.age = age
        self.height = height


class Tree(Planst):
    def __init__(self, name: str, height: int, age: int, diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = diameter
        print(f"{name} (Tree): {height}cm, {age} days, {diameter} diameter")

    def produce_shade(self):
        shade_area = 0.1 * self.height + 0.56 * self.trunk_diameter
        print(f"{self.name} provides {shade_area} square meters of shade")


class Flower(Planst):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        print(f"{name} (Flower): {height}cm, {age} days, {color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Vegetable(Planst):
    def __init__(self, name: str, height: int, age: int, season: str):
        super().__init__(name, height, age)
        self.season = season
        print(f"{name} (Vegetable): {height}cm, {age} days, {season} harvest")

    def show_nutrition(self):
        value: str
        if self.season == "summer":
            value = "Vitamin C"
        elif self.season == "fall":
            value = "Vitamin A"
        elif self.season == "winter":
            value = "Vitamin D"
        elif self.season == "spring":
            value = "Vitamin E"
        else:
            value = "Vitamin C"

        print(f"{self.name} is rich in {value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()
    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    tomato = Vegetable("Tomato", 80, 90, "summer")
    tomato.show_nutrition()
