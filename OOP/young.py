def main():
    name = get_name()
    house = get_house()
    print(f"{name.capitalize()} from {house.capitalize()} lives in a young house.")

def get_name():
    return input("What is your name? ")

def get_house():
    return input("What is your house? ")

main()