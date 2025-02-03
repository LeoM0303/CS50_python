def main() -> None:
    dataset = get_young()
    name, home = dataset

    if not name or not home:
        print("Invalid input")
        return

    print(f"{name.capitalize()} lives in {home.capitalize()}")

def get_young() -> tuple[str, str]:
    while True:
        name = input("Enter your name: ").strip()
        if not name:
            print("Invalid input")
            continue

        home = input("Enter your home: ").strip()
        if not home:
            print("Invalid input")
            continue

        return name, home

if  __name__ == "__main__":
    main()