import re
name = input("Enter your name: ").strip()

if "," in name:
    last, first = name.split(",")
    name = f"{first.strip()} {last.strip()}"
print(f'Hello, {name}')