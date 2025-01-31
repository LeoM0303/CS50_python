import re

email = input("Enter your email: ")

if re.search(".*@.*", email):
    print("Valid email")
else:
    print("Invalid email")