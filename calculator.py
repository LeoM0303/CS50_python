def new_func():
    def main():
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        
        choice = int(input("Choose an operation:\n1 - addition\n2 - subtraction\n3 - multiplication\n4 - division\n"))
        
        choice_function(x, y, choice)  
    
    def choice_function(x, y, choice):
        if choice == 1:
            print(f"Addition result: {x + y}")
        elif choice == 2:
            print(f"Subtraction result: {x - y}")
        elif choice == 3:
            print(f"Multiplication result: {x * y}")
        elif choice == 4:
            if y != 0:
                print(f"Division result: {x / y}")
            else:
                print("Error: cannot divide by zero.")
        else:
            print("Invalid choice! Please try again.")

    main()

new_func()