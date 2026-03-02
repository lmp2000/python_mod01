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
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    rose.grow(6)
    rose.ageing(6)
    print("=== Day 7 ===")
    rose.get_info()


if __name__ == "__main__":
    main()
