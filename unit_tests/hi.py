def main():
    name = input("Enter your name: ")
    hello(name.capitalize())

def hello(to="world"):
    print(f"Hello {to}")

if __name__ == "__main__":
    main()