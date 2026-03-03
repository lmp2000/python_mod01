class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")

    def __str__(self) -> str:
        return (f"{self.name} (Flower): {self.height}cm, {self.age} days,"
                f" {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = self.trunk_diameter + 28
        print(f"{self.name} provides {shade} square meters of shade\n")

    def __str__(self) -> str:
        return (f"{self.name} (Tree): {self.height}cm, {self.age} days,"
                f" {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int,
                 age: int, harvest_season: str, vitamin: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.vitamin = vitamin

    def nutrition(self) -> None:
        print(f"{self.name} is rich in vitamin {self.vitamin}")

    def __str__(self) -> str:
        return (f"{self.name} (Vegetable): {self.height}cm, {self.age} days,"
                f" {self.harvest_season} harvest")


def main() -> None:
    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 15, "purple)")
    ]
    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Oliveira", 600, 2000, 45)
    ]
    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "C"),
        Vegetable("Broculli", 50, 70, "summer", "D")
    ]

    plants = [
        lst[0] for lst in (flowers, trees, vegetables) if lst
    ]

    print("=== Garden Plant Types ===\n")
    print(plants[0])
    plants[0].bloom()
    print(plants[1])
    plants[1].produce_shade()
    print(plants[2])
    plants[2].nutrition()


if __name__ == "__main__":
    main()
