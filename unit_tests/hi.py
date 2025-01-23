def main():
    name = input("Enter your name: ")
    name = name.capitalize()
    hello(name)

def hello(to="world"):
    print(f"Hello {to}")

if __name__ == "__main__":
    main()