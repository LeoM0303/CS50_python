import re

url = input("Enter a URL: ").strip()

domain = re.sub(r"^https?://(www\.)?", "", url).split('/')[0]
print(f'Domain: {domain}')