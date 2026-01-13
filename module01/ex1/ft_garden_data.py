class Plant:
    def __init__(self) -> None:
        self.name: str
        self.height: int
        self.age: int

    def print_attributes_of_plant(self):
        print(f"{self.name} : {self.height}cm, {self.age} days old")


rose = Plant()
rose.name = "Rose"
rose.height = 24
rose.age = 30
sunflower = Plant()
sunflower.name = "Sunflower"
sunflower.height = 80
sunflower.age = 45
cactus = Plant()
cactus.name = "Cactus"
cactus.height = 15
cactus.age = 120

print("=== Garden Plant Registry ===")
rose.print_attributes_of_plant()
sunflower.print_attributes_of_plant()
cactus.print_attributes_of_plant()
