import re

email = input("Enter your email: ")

if re.search(r".+@.+\.gmail", email):
    print("Valid email")
else:
    print("Invalid email")