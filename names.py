name = []

for _ in range(3):
    name.append(input("Enter your name: "))

for name in sorted(name):
    print(f"Hello,  {name.capitalize()}")