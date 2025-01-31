import re

email = input("What`s your email? ").strip()

if re.fullmatch(r"[a-z0-9._%+-]+@gmail\.com", email, re.IGNORECASE):
    print("Valid email")
else:
    print("Invalid email")