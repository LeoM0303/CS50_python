#number similar to +380891278279

import re

phone = input("Enter Ukrainian phone number: ")

if re.fullmatch(r"\+380\d{9}$", phone):
    print("Valid Ukrainian phone number")
else:
    print("Invalid Ukrainian phone number")