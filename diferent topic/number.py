def main():
    x = get_int("Enter a number: ")
    print(f"{x} is a number")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass 

main()