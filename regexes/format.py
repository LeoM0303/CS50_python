import re

name = input("Enter your name: ").strip()
name = name.title().strip()

matches = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
if matches:
    name = f'{matches.group(2)} + " " + {matches.group(1)}'

print(f'Hello, {name}')