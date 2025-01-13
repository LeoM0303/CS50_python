name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":  # Комбінування кількох випадків
        print("You are a wizard!")
    case _:
        print("Who are you?")
