def new_func():
    square = int(input("Enter the size of the square: "))

    def main():
        print_square(square)
    
    def print_square(size):
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
    
    main()

new_func()

