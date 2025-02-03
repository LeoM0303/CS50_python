def main():
    student = get_young()
    print(f"{student[0].capitalize()} from {student[1].capitalize()} lives in a young house.")

def get_young():
    name = input("Enter your name: ")
    home = input("Enter your house: ")
    return name, home

if __name__ == "__main__":
    main()