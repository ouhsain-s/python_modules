class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def report(self):
        return (f"{self.name}: {self.height}cm")

    def score(self):
        return self.height


class FloweringPlant(Plant):

    def __init__(self, name: str, height: int, color: str, is_bloom: bool):
        super().__init__(name, height)
        self.color = color
        self.is_bloom = is_bloom

    def report(selfe):
        if (selfe.is_bloom):
            status = "(blooming)"
        else:
            status = "(not blooming)"
        return (f"{super().report()}, {selfe.color}" + status)

    def score(self):
        if (self.is_bloom):
            bonus = 5
        else:
            bonus = 0
        return super().score() + bonus


class PrizeFlower(FloweringPlant):

    def __init__(self, name: str, height: int, color: str, is_bloom: bool,
                 points: int):
        super().__init__(name, height, color, is_bloom)
        self.points = points

    def report(self):
        return super().report() + f", Prize points: {self.points}"

    def score(self):
        return super().score() + self.points


class GardenManager:

    num_of_gardens = 0

    def __init__(self, manager_name: str) -> None:
        self.manager_name = manager_name
        self.garden_plants = []
        self.total_growth = 0
        self.num_plants = 0
        GardenManager.num_of_gardens += 1

    def add_new_plant(self, name: str, height: int):

        new_plant = Plant(name, height)
        self.garden_plants.append(new_plant)
        self.num_plants += 1
        print(f"Added {name} to {self.manager_name} garden")

    def add_new_Flowering_Plant(self, name: str, height: int, color: str,
                                is_bloom: bool):

        new_plant = FloweringPlant(name, height, color, is_bloom)
        self.garden_plants.append(new_plant)
        self.num_plants += 1
        print(f"Added {name} to {self.manager_name} garden")

    def add_new_Prize_Flower(self, name: str, height: int, color: str,
                             is_bloom: bool, points: int):

        new_plant = PrizeFlower(name, height, color, is_bloom, points)
        self.garden_plants.append(new_plant)
        self.num_plants += 1
        print(f"Added {name} to {self.manager_name} garden")

    def grow_all(self):
        for plant in self.garden_plants:
            plant.grow()
            self.total_growth += 1

    def report(self):

        print(f"=== {self.manager_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.garden_plants:
            plant.report()
