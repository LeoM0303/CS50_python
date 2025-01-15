def main():
    x = get_int()
    print(x)

def get_int():
    while True:
        try:
            x = int(input("Enter a number: "))
            return x
        except ValueError:
            print("That's not a valid number!") 
        else:
            break
    return x

main()