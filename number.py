def main():
    x = get_int()
    print(f"{x} is a number")

def get_int():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            pass 

main()