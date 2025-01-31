import re

email = input("What`s your email? ").strip()

if re.fullmatch(r"[a-zA-Z0-9._%+-]+@gmail\.com", email):
    print("Valid email")
else:
    print("Invalid email")