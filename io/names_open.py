name = input("Enter your name: ")

file = open("names.txt", "a")
file.write(f"{name.capitalize()}\n")
file.close()

