class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> int:
        self.height += 1
        return 1

    def kind(self) -> str:
        return "regular"

    def score_bonus(self) -> int:
        return 0

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> bool:
        return True

    def kind(self) -> str:
        return "flowering"

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def kind(self) -> str:
        return "prize"

    def score_bonus(self) -> int:
        return self.prize_points

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}, Prize points: {self.prize_points}"


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.total_growth = 0
        self.added_count = 0

    def add_plant(self, plant: Plant) -> None:
        self.added_count += 1
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_plants(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            grow_qty = plant.grow()
            self.total_growth += grow_qty
            print(f"{plant.name} grew {grow_qty}cm")
        print()

    @staticmethod
    def validate_non_negative(value: int) -> bool:
        return value >= 0

    def validation_test(self) -> bool:
        for plant in self.plants:
            if not Garden.validate_non_negative(plant.height):
                return False
        return True

    def garden_score(self) -> int:
        score = 0
        for plant in self.plants:
            score += plant.score_bonus() + plant.height
        return score

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")
        print(f"\nPlants added: {self.added_count},"
              "Total growth: {self.total_growth}cm")

        regular, flowering, prize = 0, 0, 0
        for plant in self.plants:
            k = plant.kind()
            if k == "regular":
                regular += 1
            elif k == "flowering":
                flowering += 1
            elif k == "prize":
                prize += 1
        print(f"Plant types: {regular} regular, {flowering}",
              "flowering, {prize} prize flowers\n")


class GardenManager:
    def __init__(self) -> None:
        self.gardens = {}
        self.stats = GardenManager.GardenStats(self)

    def add_garden(self, owner: str) -> None:
        self.gardens[owner] = Garden(owner)

    def register_garden(self, garden: Garden) -> None:
        if garden.owner not in self.gardens:
            self.gardens[garden.owner] = garden
        else:
            print("Owner already exists")

    def get_garden(self, owner: str) -> Garden | None:
        return self.gardens.get(owner)

    def add_plant_to_garden(self, owner: str, plant: Plant) -> None:
        garden = self.gardens.get(owner)
        if garden is None:
            return
        garden.add_plant(plant)

    class GardenStats:
        def __init__(self, manager: "GardenManager") -> None:
            self._manager = manager

        def total_gardens(self) -> int:
            return len(self._manager.gardens)

        def total_plants(self) -> int:
            count = 0
            for garden in self._manager.gardens.values():
                count += len(garden.plants)
            return count

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> "GardenManager":
        manager = cls()
        for owner in owners:
            manager.add_garden(owner)
        return manager

    def validate(self) -> bool:
        for garden in self.gardens.values():
            if not garden.validation_test():
                return False
        return True

    def manager_output(self) -> None:
        print("Height validation test:", "True" if
              self.validate() else "False")

        score_string = []
        for garden in self.gardens.values():
            score = garden.garden_score()
            score_string.append(f"{garden.owner}: {score}")
        score_text = ", ".join(score_string)
        print(f"Garden scores - {score_text}")

        print(f"Total gardens managed: {self.stats.total_gardens()}")
