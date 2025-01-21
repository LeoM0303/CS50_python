##Import the cowsay module pip install cowsay
import cowsay

name = input("Enter your name: ")

def main():
    result = get_input()
    print(result)


def get_input():
    cowsay.cow(f'Hello, {name}')

main()