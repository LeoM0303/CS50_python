def main():
    name, home = get_young()
    print(f"{name.capitalize()} from {home.capitalize()} lives in a young house.")

def get_young():
    name = input("Enter your name: ")
    home = input("Enter your house: ")
    return name, home

if __name__ == "__main__":
    main()