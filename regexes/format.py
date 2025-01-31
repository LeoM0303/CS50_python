import re

name = input("Enter your name: ").strip()
name = name.title().strip()

matches = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
if matches:
    last, first = matches.groups()
    last = matches.group(1)
    first = matches.group(2)
    name = f'{first} {last}'

print(f'Hello, {name}')