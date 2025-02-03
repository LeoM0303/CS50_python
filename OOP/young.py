def main() -> None:
    dataset = get_young()
    if dataset is None:
        return

    name, home = dataset
    print(f"{name.capitalize()} lives in {home.capitalize()}")

def get_young() -> tuple[str, str] | None:
    while True:
        name = input("Enter your name: ").strip()
        home = input("Enter your home: ").strip()
        if not home or not name:
            print("Invalid input")
            return None

        return name, home

if  __name__ == "__main__":
    main()