class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, days):
        self.height += days

    def ageing(self, days):
        self.age += days

    def get_info(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"


def plant_factory():
    plant_ingredients = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]
    plants = [Plant(*ingredients) for ingredients in plant_ingredients]
    return plants


def main():
    plants = plant_factory()
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.get_info()}")
    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()
