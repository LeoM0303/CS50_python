# Import the cowsay module
import cowsay

# Prompt the user to input their name
name = input("Enter your name: ").strip()  # Use strip to remove any extra spaces
name = name.capitalize()  # Capitalize the first letter


def main():
    # Call the get_input function
    get_input()


def get_input():
    # Use cowsay.shark to display the message
    cowsay.shark(f'Hello, {name}!')


# Execute the main function
if __name__ == "__main__":
    main()
