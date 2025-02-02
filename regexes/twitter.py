import re

from regexes.validate import username

url = input("Enter a URL: ").strip()

username = re.sub(r"^https?://(www\.)?", "", url)

print(f'Username: {username}')
