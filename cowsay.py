##Import the cowsay module pip install cowsay
import cowsay

name = input("Enter your name: ")
name = name.capitalize()

def main():
    result = get_input()
    print(result)


def get_input():
    cowsay.tux(f'Hello, {name}')

main()