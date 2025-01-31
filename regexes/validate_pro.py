import re

email = input("What`s your email? ").strip()

if re.search(r".+@.+\.gmail$", email):
    print("Valid email")
else:
    print("Invalid email")