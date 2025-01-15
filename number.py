try:
    x = int(input("Enter a number: "))
    print(f'You entered {x}')
except ValueError:
    print("That's not a number!")