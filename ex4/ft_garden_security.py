class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        print(f"Plant created: {self.name}")
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attemped: height {height} [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attemped: age {age} [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def __str__(self) -> str:
        cm = self.get_height()
        days = self.get_age()
        return f"{self.name} ({cm}cm, {days} days)"

def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 25, 30)
    print("\n")
    rose.set_height(-5)
    print("\n")
    print(f"Current plant: {rose}")

if __name__ == "__main__":
    main()
