def main():
    x = int(input("Enter a number: "))
    print("Square your number", f'{square(x)}')
    
def square(x):
    return x * x

main()