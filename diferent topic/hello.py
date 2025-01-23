def main():
    name = input("What is your name? ")
    hello(name.capitalize())
    
def hello(to='world'):
    print(f"Hello {to}")
    
main()