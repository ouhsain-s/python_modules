class Planst:
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


class FloweringPlant(Planst):

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

    def report(selfe):
        return super().report() + f", Prize points: {selfe.points}"

    def score(self):
        return super().score() + self.points
